# Output Style and Data Contract

Use this reference immediately before drafting. The default output is concise and resembles a practical journal review rather than an exhaustive section-by-section audit.

## Contents

- Output order
- Chinese assessment
- Confidential editor note
- Comments to authors
- Concision rules
- Punctuation rules
- Prose quality
- Review JSON
- DOCX content

## Output order

1. Chinese assessment
2. Confidential comments to the editor in English
3. Comments to the authors in English
4. English author-facing DOCX

## Chinese assessment

State the recommendation, confidence, and two to four decisive reasons. Mention missing or unreadable evidence and any mismatch between a user-requested recommendation and the manuscript evidence. Keep the assessment concise.

## Confidential editor note

- State the recommended outcome and the decisive validity or contribution reasons.
- Ground the note only in supplied files and verified public information.
- Do not imply hidden editor knowledge or another reviewer's opinion.
- Do not copy the note into the author report.

## Comments to authors

Use this structure.

1. One short summary paragraph of one or two sentences. Identify only the question, method or design, and principal claimed result needed to recognize the paper.
2. One separate sentence that explicitly states the recommended decision. Keep it direct and do not add a second overview of the paper.
3. Numbered concerns arranged in the order of the manuscript. Normally move from the introduction and literature review through theory, methods or model, results, discussion, Management Insights, conclusions, and limitations.

Use eight to ten concerns as the normal range for Reject and Major Revision. Use three to six concerns as the normal range for Minor Revision. These are calibration ranges, not quotas. Use fewer when the evidence supports fewer, and use more than ten when a viable manuscript contains more than ten distinct high-value problems. Never split, repeat, or invent concerns to meet a range. Record `concern_count_rationale` when the count falls outside the normal range.

Format each concern as a real numbered item. Begin the comment immediately after the number. Do not add a concern heading.

```text
1. The manuscript does not yet distinguish the proposed mechanism from existing service spillover explanations. Please identify the prediction that differs from those explanations and show where the model or evidence tests it.
```

Each concern should establish:

- The issue
- The manuscript evidence or verified location
- The consequence for contribution, validity, interpretation, or presentation
- A feasible requested action

Keep those four elements in the internal fields. The author-facing `comment` should synthesize only what the author needs to understand and address the concern.

Assign each concern an internal `manuscript_order` value that reflects the first manuscript section where the issue can be understood and repaired. Values must be positive and nondecreasing. The value is validation metadata and does not appear in the author-facing report.

Do not add labels such as Issue, Evidence, Consequence, or Action to every concern. Write integrated reviewer prose.

## Concision rules

- Do not target a uniform word count. Let each concern be as short or long as its scientific content requires.
- A simple issue may be one direct sentence. Do not add evidence, consequence, or explanatory framing when naming the correction is sufficient.
- A complex issue may begin with a short phrase-like sentence that identifies the problem, followed by the minimum reasoning needed to make the criticism sound and usable.
- Vary sentence length and structure naturally. Avoid making every concern follow the same issue, evidence, consequence, action cadence.
- Point out a problem without fully diagnosing or solving it when the evidence does not require more detail.
- Remove long introductions, descriptive modifiers, repeated reasoning, and inventories of similar omissions.
- Summarize related missing details at the appropriate level. Prefer `The model requires clearer specification` to a long list when the list does not change the criticism.
- If a location is useful, state it directly, such as `Section 3 does not justify this assumption.` Do not add a separate location sentence by habit.
- Keep the tone formal, direct, and evidence-based. Do not use ornate language to make a concern appear more serious.
- When a formula is necessary, put the formula in `equations`. The DOCX must contain a native Word equation object. Do not spell out mathematical operators and symbols in prose.

## Punctuation rules

- Do not use U+2014 em dash or U+2013 en dash in generated reviewer prose.
- Do not use ASCII colon or Chinese fullwidth colon as a sentence connector.
- Do not end routine labels with a colon.
- Prefer a new sentence, comma, semicolon, parentheses, or a label followed by a new line.
- Do not make sentences longer or less readable merely to avoid punctuation.
- Preserve punctuation in source-faithful titles, quotations, formulas, identifiers, URLs, DOI strings, times, and required machine-readable syntax.
- Preserve necessary ASCII hyphens in manuscript IDs, compound terms, ranges, and mathematical notation.

## Prose quality

- Prefer specific diagnosis to generic advice.
- Identify the missing literature strand and its role instead of saying only that more references are needed.
- State why an additional analysis is necessary and which threat it addresses.
- Do not overstate certainty.
- Avoid repeated openings and boilerplate across concerns.
- Mention language problems briefly and representatively.
- Describe visual irregularities through observable features such as inconsistent edges, typography, resolution, alignment, or compression. Do not use colloquial wording or infer image manipulation without evidence. When the cause is uncertain, state that the figure appears visually inconsistent and request verification against the original output.
- Do not include tool citations, source tokens, severity metadata, or private reasoning in the DOCX.
- Do not write as the authors.
- Do not write a rebuttal, revision plan, or editorial decision letter unless the user asks for that document type.

## Review JSON

Use UTF-8 JSON with this top-level structure. Empty optional values may be empty strings or empty arrays.

```json
{
  "article_type": "original research",
  "review_round": "initial",
  "target_journal": "",
  "recommendation": "Major Revision",
  "recommendation_source": "independent",
  "confidence": "high",
  "manuscript_summary": "One or two concise English sentences.",
  "author_overall_assessment": "One English sentence that states the recommended decision.",
  "concern_count_rationale": "",
  "chinese_assessment": "Concise Chinese assessment.",
  "confidential_editor_note": "Confidential English note.",
  "concerns": [
    {
      "id": 1,
      "severity": "major",
      "issue": "Specific issue sentence.",
      "evidence": "Verified manuscript evidence.",
      "consequence": "Why the issue matters.",
      "requested_action": "Feasible requested action.",
      "location": "Section 2",
      "manuscript_order": 20,
      "comment": "Natural author-facing comment whose length follows the issue.",
      "equations": []
    }
  ],
  "evidence_locations": ["Section 2"],
  "verification_sources": [],
  "protected_source_spans": []
}
```

Allowed values:

- `article_type` uses `original research`, `review article`, or `hybrid`
- `review_round` uses `initial` or `revision`
- `recommendation` uses `Accept`, `Minor Revision`, `Major Revision`, or `Reject`
- `recommendation_source` uses `independent` or `user`
- `confidence` uses `high`, `medium`, or `low`
- concern `severity` uses `fatal`, `major`, or `minor`

Use any consistent positive scale for `manuscript_order`, such as 10 for the introduction, 20 for the literature review, 30 for theory, 40 for methods or model, 50 for results, 60 for discussion, 70 for Management Insights, 80 for conclusions, and 90 for limitations. Adapt the scale to the actual manuscript structure.

Optional internal field `length_rationale` may explain an unusually long comment. It never appears in the DOCX.

Place exact source titles, quotations, formulas, URLs, DOI strings, times, or identifiers that legitimately contain restricted punctuation in `protected_source_spans`. Protection is an accuracy exception, not a way to bypass style rules.

## DOCX content

The DOCX contains only `manuscript_summary`, `author_overall_assessment`, each numbered author-facing `comment`, and any native Word equations. It does not contain concern headings, the internal issue, evidence, consequence, requested action, location, recommendation metadata, concern-count rationale, manuscript-order metadata, Chinese assessment, confidential editor note, evidence ledger, verification list, or protected-span metadata.
