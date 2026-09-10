# OM Reviewer

[简体中文](README_CN.md)

`om-reviewer` is a Codex skill for reviewing original research and review manuscripts in operations management, economics and management, artificial intelligence, blockchain, logistics, supply chain management, ESG, CSR, and related interdisciplinary fields. It is designed for rigorous SCI Q1 peer review while keeping author-facing comments concise, direct, and evidence-based.

## Capabilities

- Reviews empirical studies, theoretical models, optimization, game theory, Markov processes, simulations, machine learning studies, case studies, mixed-method research, and review articles.
- Evaluates research motivation, theoretical contribution, method applicability, evidence, conclusions, practical relevance, reproducibility, integrity signals, references, figures, and language.
- Tests whether the focal technology, construct, or solution is specifically connected to an actor, decision, mechanism, operational problem, and outcome.
- Checks whether numerical parameters are supported by literature, data, institutional facts, or documented cases.
- Evaluates Management Insights and equivalent sections against realistic decisions and evidence boundaries.
- Supports initial review and revision-round review.
- Produces a concise Chinese assessment, a confidential English editor note, English comments to authors, and an author-facing English DOCX report.
- Validates recommendation consistency, punctuation, concern order, duplication, and prohibited reviewer identities.

## Supported outputs

The standard workflow returns four outputs.

1. A concise Chinese assessment with a recommendation and decisive reasons.
2. A confidential English note to the editor.
3. Journal-ready English comments to the authors.
4. An English DOCX containing only the author-facing comments.

The recommendation is advice to the editor. It is not an editorial decision.

## Repository structure

```text
om-reviewer/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── review-report-template.docx
├── references/
└── scripts/
    ├── build_review_docx.py
    └── validate_review_output.py
```

`SKILL.md` contains the core workflow and routes to detailed references only when they are relevant. The scripts provide deterministic validation and DOCX generation. Keep the complete directory together because the skill depends on its references, scripts, metadata, and template.

## Requirements

- ChatGPT desktop with Codex, Codex CLI, or the Codex IDE extension
- PDF and Documents capabilities for complete manuscript inspection
- Python 3.10 or later when using the included validation and DOCX scripts
- `python-docx` for DOCX generation

Install the Python dependency when your Codex environment does not already provide it.

```powershell
python -m pip install -r requirements.txt
```

For local release validation, `requirements-dev.txt` also installs `PyYAML`, which is required by the Skill Creator validator.

## Installation scope

Choose one installation scope. Do not install the same `om-reviewer` skill in several discovered locations because Codex may show duplicate skills with the same frontmatter name.

### Personal installation

Use a personal installation when you want the skill available across projects. The bundled `$skill-installer` installs into `$CODEX_HOME/skills/om-reviewer`. If `CODEX_HOME` is unset, its default is `~/.codex/skills/om-reviewer`.

OpenAI Docs also documents `$HOME/.agents/skills/om-reviewer` as a user-managed filesystem location. Use one personal location, not both.

### Project installation

Use a project installation when only one repository should discover the skill.

```text
<PROJECT_ROOT>/.agents/skills/om-reviewer
```

Commit that directory only when the skill is intended for every authorized user of the project. Never place confidential manuscript files beside it.

## Recommended installation with Skill Installer

The Skill Installer downloads public repositories directly and can fall back to Git when necessary. Private repositories require existing Git credentials or an appropriate `GITHUB_TOKEN` or `GH_TOKEN`. The installer does not overwrite an existing destination.

Because `SKILL.md` is at this repository's root, the repository path is `.` and the destination name must be `om-reviewer`.

### ChatGPT desktop with Codex

1. Open Codex in the ChatGPT desktop app.
2. Start a new task.
3. Paste the repository URL and the following request.

```text
Use $skill-installer to install om-reviewer from this GitHub repository.
The skill is at the repository root. Use path . and install it with the name om-reviewer.
```

4. Approve the network download when Codex requests permission.
5. Start a new task after installation. Restart the app if the skill does not appear.
6. Open Skills in the sidebar or invoke the skill with `$om-reviewer`.

### Codex CLI

Start Codex and give it the same installation request.

```text
$skill-installer

Install om-reviewer from https://github.com/anan-915/om-reviewer.git.
The skill is at path . and must be installed with the name om-reviewer.
```

After installation, start a new Codex session. Run `/skills` to confirm discovery, or type `$om-reviewer` in a prompt.

Advanced users can call the bundled installer directly.

Windows PowerShell

```powershell
$codexHomePath = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$installerPath = Join-Path $codexHomePath "skills\.system\skill-installer\scripts\install-skill-from-github.py"
python $installerPath --repo "anan-915/om-reviewer" --path "." --name "om-reviewer"
```

macOS or Linux

```bash
codex_home_path="${CODEX_HOME:-$HOME/.codex}"
python "$codex_home_path/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo "anan-915/om-reviewer" --path "." --name "om-reviewer"
```

### Codex IDE extension

The IDE extension uses the same filesystem skill locations as Codex CLI.

1. Install the skill once with `$skill-installer` in a Codex task or with the direct installer command above.
2. Start a new IDE chat after installation.
3. Use `/skills` or type `$om-reviewer` to confirm that it is available.
4. Restart the IDE or reload its window if the updated skill is not detected.

## Manual Git installation

A Git clone is useful when you want simple updates with `git pull`.

### Personal installation on Windows

```powershell
$codexHomePath = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$skillsPath = Join-Path $codexHomePath "skills"
New-Item -ItemType Directory -Force -Path $skillsPath | Out-Null
git clone https://github.com/anan-915/om-reviewer.git (Join-Path $skillsPath "om-reviewer")
```

### Personal installation on macOS or Linux

```bash
codex_home_path="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$codex_home_path/skills"
git clone https://github.com/anan-915/om-reviewer.git "$codex_home_path/skills/om-reviewer"
```

### Project-specific installation

Run this command from the project root.

```bash
mkdir -p .agents/skills
git clone https://github.com/anan-915/om-reviewer.git .agents/skills/om-reviewer
```

Restart Codex or start a new session if the skill is not immediately available.

## Updating

Use the update method that matches the original installation method.

### Updating a Git clone

Windows PowerShell

```powershell
$codexHomePath = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
git -C (Join-Path $codexHomePath "skills\om-reviewer") pull --ff-only
```

macOS or Linux

```bash
codex_home_path="${CODEX_HOME:-$HOME/.codex}"
git -C "$codex_home_path/skills/om-reviewer" pull --ff-only
```

For a project-specific clone, run `git -C .agents/skills/om-reviewer pull --ff-only` from the project root.

Do not edit the installed clone directly. Keep your development changes in a separate fork or working copy so that `git pull --ff-only` remains predictable.

### Updating a Skill Installer or copied installation

The bundled Skill Installer stops when the destination already exists. It does not perform an in-place update.

1. Move the installed `om-reviewer` directory to a backup location outside every discovered skills directory.
2. Run the Skill Installer again with the same repository, path `.`, and name `om-reviewer`.
3. Start a new Codex task and run a non-confidential test.
4. Delete the backup only after the new installation has been verified.

Replace the whole directory instead of copying new files over the old installation. This prevents files removed upstream from remaining active locally.

## Verifying the installation

1. Confirm that the installed directory contains `SKILL.md`, `references`, `scripts`, `assets`, and `agents/openai.yaml`.
2. Start a new Codex task or restart Codex.
3. Run `/skills` where available or type `$om-reviewer`.
4. Test with a synthetic or non-confidential manuscript first.
5. If DOCX generation is needed, confirm that the following commands load correctly.

```powershell
python scripts/validate_review_output.py --help
python scripts/build_review_docx.py --help
```

Standalone filesystem skills are supported by ChatGPT desktop with Codex, Codex CLI, and the Codex IDE extension. A standalone GitHub skill is not directly installed into ordinary ChatGPT web or mobile chat. Distribution to those surfaces requires different packaging, such as a supported plugin.

## Usage

Invoke the skill explicitly with `$om-reviewer`, attach a PDF or DOCX manuscript, and state the target journal, review round, and preferred recommendation when available.

```text
Use $om-reviewer to review this manuscript for an SCI Q1 journal.
This is an initial review, and I currently lean toward Major Revision.
```

The requested recommendation controls the intended framing but does not authorize fabricated evidence. If the manuscript evidence conflicts materially with the requested recommendation, the skill is instructed to disclose the mismatch.

Validate a structured review and build the author-facing DOCX with the included scripts.

```powershell
python scripts/validate_review_output.py review.json --strict
python scripts/build_review_docx.py review.json review-report.docx
```

The DOCX builder uses `assets/review-report-template.docx` by default.

## Confidentiality and responsible use

- Treat every unpublished manuscript, supplement, response letter, and reviewer report as confidential.
- Do not include unpublished titles, author names, distinctive claims, or manuscript text in public search queries.
- Do not commit manuscripts, reviewer reports, generated reviews, extracted text, or temporary render files to this repository.
- Check the journal, publisher, institution, and review agreement before using AI assistance. If the governing policy prohibits AI use, do not use this skill for substantive review.
- Review outputs are recommendations. Editors retain responsibility for publication decisions.
- Report observable integrity concerns cautiously. Do not claim misconduct without adequate evidence.

The repository intentionally excludes historical reviewer reports used during private development and calibration. No unpublished manuscript or identifiable review report is distributed with this project.

## Limitations

- The skill cannot replace domain judgment, independent statistical assessment, legal advice, ethics review, or an editor's decision.
- Output quality depends on complete and readable manuscript files.
- External novelty and policy claims may require current authoritative verification.
- Method references provide review signals rather than automatic thresholds or verdicts.

## Acknowledgements

This project benefited from studying the public design, organization, and distribution practices of [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills). We thank Yuan Yizhe and the project's contributors for sharing their work with the research and open-source communities.

`om-reviewer` is independently developed and does not copy or redistribute the private source materials, manuscript data, or project-specific content of other projects.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE).

## Independence

This is an independent project. It is not affiliated with, endorsed by, or an official product of OpenAI, Elsevier, any journal, or any publisher. References to external guidance and projects identify public resources and do not imply endorsement.

For current Codex skill locations and invocation behavior, consult the [official OpenAI documentation](https://learn.chatgpt.com/docs/build-skills).
