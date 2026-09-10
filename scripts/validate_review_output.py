#!/usr/bin/env python3
"""Validate the structured output produced by the om-reviewer skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = {
    "article_type",
    "review_round",
    "target_journal",
    "recommendation",
    "recommendation_source",
    "confidence",
    "manuscript_summary",
    "author_overall_assessment",
    "concern_count_rationale",
    "chinese_assessment",
    "confidential_editor_note",
    "concerns",
    "evidence_locations",
    "verification_sources",
    "protected_source_spans",
}

REQUIRED_CONCERN_FIELDS = {
    "id",
    "severity",
    "issue",
    "evidence",
    "consequence",
    "requested_action",
    "location",
    "manuscript_order",
    "comment",
    "equations",
}

ALLOWED = {
    "article_type": {"original research", "review article", "hybrid"},
    "review_round": {"initial", "revision"},
    "recommendation": {"Accept", "Minor Revision", "Major Revision", "Reject"},
    "recommendation_source": {"independent", "user"},
    "confidence": {"high", "medium", "low"},
    "severity": {"fatal", "major", "minor"},
}

FORBIDDEN_ROLE_PATTERNS = [
    re.compile(
        r"\b(?:statistics|statistical|ethics|ethical|clinical|methods?|methodological|senior|expert)\s+reviewer\b",
        re.IGNORECASE,
    ),
    re.compile(r"\breviewer\s+(?:no\.?\s*)?\d+\b", re.IGNORECASE),
    re.compile(r"\b(?:as|speaking as)\s+(?:an?\s+)?\w+\s+reviewer\b", re.IGNORECASE),
]

VAGUE_ACTION_PATTERNS = [
    re.compile(r"^(?:please\s+)?(?:add|include)\s+more\s+(?:references|literature)\.?$", re.IGNORECASE),
    re.compile(r"^(?:please\s+)?(?:strengthen|improve|expand)\s+(?:the\s+)?(?:analysis|discussion|methods?|paper)\.?$", re.IGNORECASE),
    re.compile(r"^(?:please\s+)?provide\s+more\s+(?:detail|details|explanation|analysis)\.?$", re.IGNORECASE),
]

URL_RE = re.compile(r"https?://[^\s)\]}]+", re.IGNORECASE)
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
TIME_RE = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\b")
STABLE_ID_RE = re.compile(r"\b[A-Z][A-Z0-9-]{2,}:[A-Z0-9._/-]+\b")
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*")

DECISION_PATTERNS = {
    "Accept": re.compile(r"\b(?:accept|suitable for publication)\b", re.IGNORECASE),
    "Minor Revision": re.compile(r"\bminor revisions?\b", re.IGNORECASE),
    "Major Revision": re.compile(r"\bmajor revisions?\b", re.IGNORECASE),
    "Reject": re.compile(r"\b(?:reject|rejection|not suitable for publication)\b", re.IGNORECASE),
}

NORMAL_CONCERN_RANGES = {
    "Reject": (8, 10),
    "Major Revision": (8, 10),
    "Minor Revision": (3, 6),
}


def _text(value: Any) -> str:
    return value if isinstance(value, str) else ""


def _normalize(value: str) -> str:
    value = value.lower()
    value = re.sub(r"\s+", " ", value)
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff ]", "", value)
    return value.strip()


def _mask_exemptions(text: str, protected: list[str]) -> str:
    masked = text
    for span in sorted((s for s in protected if s), key=len, reverse=True):
        masked = masked.replace(span, "<PROTECTED>")
    masked = URL_RE.sub("<URL>", masked)
    masked = DOI_RE.sub("<DOI>", masked)
    masked = TIME_RE.sub("<TIME>", masked)
    masked = STABLE_ID_RE.sub("<ID>", masked)
    return masked


def _walk_generated_strings(payload: dict[str, Any]) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    for field in (
        "manuscript_summary",
        "author_overall_assessment",
        "chinese_assessment",
        "confidential_editor_note",
    ):
        if field in payload:
            items.append((field, _text(payload.get(field))))
    concerns = payload.get("concerns")
    if isinstance(concerns, list):
        for index, concern in enumerate(concerns, 1):
            if not isinstance(concern, dict):
                continue
            items.append((f"concerns[{index}].comment", _text(concern.get("comment"))))
    return items


def _sentence_count(text: str) -> int:
    text = text.strip()
    if not text:
        return 0
    endings = re.findall(r"[.!?](?=(?:[\"')\]]*)\s|(?:[\"')\]]*)$)", text)
    return len(endings) if endings else 1


def validate_payload(payload: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    missing = sorted(REQUIRED_FIELDS - set(payload))
    if missing:
        errors.append(f"Missing required top-level fields: {', '.join(missing)}")

    for field, allowed in ALLOWED.items():
        if field == "severity":
            continue
        value = payload.get(field)
        if value not in allowed:
            errors.append(f"Invalid {field}: {value!r}. Allowed values are {sorted(allowed)}")

    for field in (
        "target_journal",
        "manuscript_summary",
        "author_overall_assessment",
        "concern_count_rationale",
        "chinese_assessment",
        "confidential_editor_note",
    ):
        if field in payload and not isinstance(payload[field], str):
            errors.append(f"{field} must be a string")

    recommendation = payload.get("recommendation")
    summary = _text(payload.get("manuscript_summary")).strip()
    summary_sentences = _sentence_count(summary)
    if not summary:
        errors.append("manuscript_summary must be non-empty")
    elif not 1 <= summary_sentences <= 2:
        errors.append(f"manuscript_summary must contain one or two sentences, found {summary_sentences}")

    assessment = _text(payload.get("author_overall_assessment")).strip()
    if not assessment:
        errors.append("author_overall_assessment must be a non-empty second paragraph")
    elif recommendation in DECISION_PATTERNS and not DECISION_PATTERNS[recommendation].search(assessment):
        errors.append("author_overall_assessment must explicitly state the recommended decision")
    if assessment and _sentence_count(assessment) != 1:
        errors.append("author_overall_assessment must contain exactly one sentence")

    for field in ("evidence_locations", "verification_sources", "protected_source_spans"):
        value = payload.get(field)
        if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
            errors.append(f"{field} must be an array of strings")

    protected_raw = payload.get("protected_source_spans", [])
    protected = protected_raw if isinstance(protected_raw, list) else []

    concerns = payload.get("concerns")
    if not isinstance(concerns, list):
        errors.append("concerns must be an array")
        concerns = []

    if payload.get("recommendation") != "Accept" and not concerns:
        errors.append("A non-Accept recommendation requires at least one concern")

    normal_range = NORMAL_CONCERN_RANGES.get(recommendation)
    if normal_range and not normal_range[0] <= len(concerns) <= normal_range[1]:
        rationale = _text(payload.get("concern_count_rationale")).strip()
        if not rationale:
            errors.append(
                f"{recommendation} normally uses {normal_range[0]} to {normal_range[1]} concerns. "
                "Provide concern_count_rationale when departing from that range"
            )
    ids: list[int] = []
    manuscript_orders: list[int] = []
    bodies: list[tuple[int, str]] = []
    severities: list[str] = []
    for index, concern in enumerate(concerns, 1):
        if not isinstance(concern, dict):
            errors.append(f"Concern {index} must be an object")
            continue
        missing_concern = sorted(REQUIRED_CONCERN_FIELDS - set(concern))
        if missing_concern:
            errors.append(f"Concern {index} is missing fields: {', '.join(missing_concern)}")
        if _text(concern.get("heading")).strip():
            errors.append(f"Concern {index} must not include an author-facing heading")

        cid = concern.get("id")
        if not isinstance(cid, int) or cid < 1:
            errors.append(f"Concern {index} id must be a positive integer")
        else:
            ids.append(cid)

        severity = concern.get("severity")
        if severity not in ALLOWED["severity"]:
            errors.append(f"Concern {index} has invalid severity: {severity!r}")
        else:
            severities.append(severity)

        manuscript_order = concern.get("manuscript_order")
        if not isinstance(manuscript_order, int) or isinstance(manuscript_order, bool) or manuscript_order < 1:
            errors.append(f"Concern {index} manuscript_order must be a positive integer")
        else:
            manuscript_orders.append(manuscript_order)

        for field in ("issue", "evidence", "consequence", "requested_action"):
            value = _text(concern.get(field)).strip()
            if not value:
                errors.append(f"Concern {index} requires non-empty {field}")

        comment = _text(concern.get("comment")).strip()
        if not comment:
            errors.append(f"Concern {index} requires a non-empty author-facing comment")
        comment_words = len(WORD_RE.findall(comment))
        if comment_words > 180:
            errors.append(f"Concern {index} comment is unusually long at {comment_words} words")
        elif comment_words > 130 and not _text(concern.get("length_rationale")).strip():
            warnings.append(f"Concern {index} comment exceeds 130 words without length_rationale")
        if "The relevant material appears in" in comment:
            warnings.append(f"Concern {index} uses an unnecessary location boilerplate sentence")

        equations = concern.get("equations")
        if not isinstance(equations, list) or any(not isinstance(item, str) or not item.strip() for item in equations):
            errors.append(f"Concern {index} equations must be an array of non-empty strings")
        for optional_field in ("length_rationale",):
            if optional_field in concern and not isinstance(concern[optional_field], str):
                errors.append(f"Concern {index} {optional_field} must be a string")

        action = _text(concern.get("requested_action")).strip()
        if any(pattern.fullmatch(action) for pattern in VAGUE_ACTION_PATTERNS):
            warnings.append(f"Concern {index} requested_action is too generic")
        if not _text(concern.get("location")).strip():
            warnings.append(f"Concern {index} has no verified manuscript location")

        bodies.append((index, _normalize(comment)))

    if ids and (len(ids) != len(set(ids)) or sorted(ids) != list(range(1, len(ids) + 1))):
        errors.append("Concern ids must be unique and sequential starting at 1")
    if len(manuscript_orders) == len(concerns) and manuscript_orders != sorted(manuscript_orders):
        errors.append("Concerns must be arranged in nondecreasing manuscript_order")

    for pos, (left_index, left_body) in enumerate(bodies):
        for right_index, right_body in bodies[pos + 1 :]:
            if left_body and right_body and SequenceMatcher(None, left_body, right_body).ratio() >= 0.86:
                errors.append(f"Concerns {left_index} and {right_index} appear duplicative")

    for label, value in _walk_generated_strings(payload):
        masked = _mask_exemptions(value, protected)
        if "\u2013" in masked or "\u2014" in masked:
            errors.append(f"{label} contains a forbidden en dash or em dash")
        if ":" in masked or "：" in masked:
            errors.append(f"{label} contains an unprotected colon that may be acting as a sentence connector")
        for pattern in FORBIDDEN_ROLE_PATTERNS:
            if pattern.search(masked):
                errors.append(f"{label} appears to invent a reviewer identity or role")

    author_text = " ".join(
        [
            _text(payload.get("manuscript_summary")),
            _text(payload.get("author_overall_assessment")),
        ]
        + [_text(concern.get("comment")) for concern in concerns if isinstance(concern, dict)]
    )
    confidential = _normalize(_text(payload.get("confidential_editor_note")))
    if len(confidential) >= 40 and confidential in _normalize(author_text):
        errors.append("The confidential editor note appears verbatim in the author-facing content")

    if recommendation == "Accept" and concerns:
        warnings.append("Accept normally should not include substantive concerns")
    if recommendation == "Minor Revision" and any(severity in {"fatal", "major"} for severity in severities):
        errors.append("Minor Revision is inconsistent with fatal or major concern severity")
    if recommendation == "Reject" and concerns and "fatal" not in severities:
        warnings.append("Reject has no concern marked fatal. Recheck decision calibration")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 review JSON")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    try:
        payload = json.loads(args.input.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: Could not read review JSON: {exc}", file=sys.stderr)
        return 1
    if not isinstance(payload, dict):
        print("ERROR: Top-level JSON value must be an object", file=sys.stderr)
        return 1

    errors, warnings = validate_payload(payload)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors or (args.strict and warnings):
        return 1
    print(f"PASS: {args.input} satisfies the om-reviewer output contract")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
