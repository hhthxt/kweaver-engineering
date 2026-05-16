[中文](./README.zh.md) | English

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

# KWeaver Engineering

AI engineering capability tools and skill packages for KWeaver BKN projects.

## Available Skills

### `bkn-requirement`

`bkn-requirement` is a requirement discovery skill for KWeaver BKN projects. It helps AI engineers and business experts turn interviews, meeting notes, draft PRDs, BRDs, process descriptions, and system/data materials into a business-scenario-centered PRD.

It is designed for the stage before formal BKN modeling.

## Background

In BKN projects, the hardest problem is often not writing the model file. The earlier problem is making the business requirement clear enough:

- What business scenario is being solved?
- Who uses the capability?
- What is the current workflow?
- What inputs and outputs does the user expect?
- What business rules and exception cases matter?
- Which systems, forms, reports, and data sources are involved?
- What permissions, approvals, and audit boundaries are required?
- How should the result be accepted by business users?

`bkn-requirement` focuses on this upstream discovery work. It keeps the main PRD in business language, then produces a concise `BKN_Creator` handoff summary for downstream modeling.

## Service Scenarios

Use `bkn-requirement` when you need to:

- Prepare for a business expert interview.
- Process interview notes or meeting transcripts.
- Convert a rough idea, PRD, BRD, or process document into a standard PRD.
- Split a complex requirement into business scenarios.
- Identify missing business rules, data sources, permissions, and acceptance cases.
- Generate follow-up questions for AI engineers.
- Produce a handoff summary for `BKN_Creator`.

## Relationship With `BKN_Creator`

`bkn-requirement` and `BKN_Creator` work in sequence:

```text
Business idea / interview / draft PRD
  -> bkn-requirement
  -> Business-scenario-centered PRD
  -> BKN_Creator handoff summary
  -> BKN_Creator
  -> BKN modeling, binding, testing, and validation
```

`bkn-requirement` does not create `.bkn` files, bind data sources or platform data views, push networks, or execute platform operations. Those are downstream responsibilities of `BKN_Creator` and related KWeaver engineering tools.

## AI Agent Skills

Install the skill from this repository with `npx skills`:

```bash
npx skills add https://github.com/kweaver-ai/kweaver-engineering \
  --skill bkn-requirement
```

`bkn-requirement` — a requirement discovery skill for KWeaver BKN projects. It helps AI engineers turn interviews, meeting notes, draft PRDs, BRDs, process descriptions, and system/data materials into a business-scenario-centered PRD, then produce a `BKN_Creator` handoff summary. See `skills/bkn-requirement/SKILL.md`.

`npx skills` installs the selected skill into the skills location supported by the developer's current AI agent environment. Restart your agent session after installation so the skill list refreshes.

### Skill Source

This repository publishes `bkn-requirement` as a standard self-contained Agent Skill directory. The repository also keeps a shared source copy of the BKN methodology under `skills/common/` for cross-skill reuse:

```text
skills/
  common/
    bkn-methodology.md
  bkn-requirement/
    SKILL.md
    agents/openai.yaml
    assets/
    references/
      bkn-methodology.md
```

`bkn-requirement` uses `references/bkn-methodology.md` at runtime, so `npx skills add ... --skill bkn-requirement` can install the selected skill by itself. `skills/common/bkn-methodology.md` is the repository-level source copy; maintainers should sync it into `skills/bkn-requirement/references/bkn-methodology.md` before publishing.

### Manual Fallback (Advanced)

If the target environment cannot use `npx skills`, clone the repository and copy `skills/bkn-requirement/` into the skills directory documented by that agent. Different agents scan different locations, so follow the target agent's official documentation.

```bash
git clone https://github.com/kweaver-ai/kweaver-engineering.git
cd kweaver-engineering
```

Expected installed layout:

```text
<skills-root>/
  bkn-requirement/
    SKILL.md
    agents/
    assets/
    references/
      bkn-methodology.md
```

If the installed `bkn-requirement/references/bkn-methodology.md` file is missing, the install is incomplete and should be refreshed.

Cursor, Codex, OpenClaw, and other agents can discover this skill only if they support `SKILL.md`-based skills and scan the directory written by `npx skills` or by the agent configuration.

### Development Guide: Common References

When a new skill needs methodology or shared knowledge from `skills/common/`, use a "shared source + skill-local distribution snapshot" structure:

```text
skills/
  common/
    bkn-methodology.md              # shared source, edited by maintainers
  <skill-name>/
    SKILL.md
    references/
      bkn-methodology.md            # distribution snapshot used at runtime
```

Rules:

- Runtime instructions in `SKILL.md` should reference only files inside the skill, such as `references/bkn-methodology.md`.
- Published skills must not depend on `../common/...`, because `npx skills add --skill <skill-name>` may install only the selected skill directory.
- Maintain shared methodology in `skills/common/<file>.md`, then sync it into every skill that needs it before publishing.
- If multiple skills reuse the same common file, each skill must carry its own distribution snapshot.

Register copy relationships in:

```text
skills/common/reference-sync.json
```

Example:

```json
{
  "copies": [
    {
      "source": "skills/common/bkn-methodology.md",
      "dest": "skills/bkn-requirement/references/bkn-methodology.md",
      "skill": "bkn-requirement",
      "description": "BKN methodology runtime snapshot for the requirement discovery skill."
    }
  ]
}
```

When a new skill reuses a common file, add one entry to `copies`.

Sync all registered distribution snapshots:

```bash
skills/common/sync-common-references.py
```

Before publishing, verify that distribution snapshots match the common source:

```bash
skills/common/sync-common-references.py --check
```

### Use directly from a project

You can also keep the skill in a project repository under:

```text
skills/
  bkn-requirement/
```

Keeping `skills/common/bkn-methodology.md` in the same repository is recommended for development, but runtime use does not require it because `bkn-requirement` carries its own methodology snapshot.

When the agent has access to the project workspace, invoke it by name:

```text
Use $bkn-requirement to generate a standard PRD from this interview note.
```

## How To Use

### 0. Project folder

Create one folder per customer or project so presales, delivery, and engineering materials do not mix:

```text
docs/requirements/prj-<customer-or-project-short-name>/
```

Suggested names:

| Document type | Naming format |
|---|---|
| Research outline | `<project>-round-X-research-outline.md` |
| Meeting memo | `YYYYMMDD-<project>-round-X-meeting-memo.md` |
| Validation output | `<project>-prd-round-X-validation.md` |
| PRD | `<project>-PRD vX.Y.md` |

Archive each round's input materials under:

```text
docs/requirements/prj-<customer-or-project-short-name>/inputs/round-XX/
```

If a user-specified input file is outside the project folder, the skill must copy it into the current round's `inputs/round-XX/` folder before generating the validation output or PRD, without moving the original file. If the input file is already inside the project folder, copying is optional, but the skill should create or update `source-manifest.md` to record the input source.

`source-manifest.md` must only record archive actions that actually happened. Any file marked as copied must have an existing archived path. If copying fails or the path is inaccessible, the manifest and final output must say so instead of marking it as copied.

Recommended input names:

| Input type | Naming format |
|---|---|
| Research outline | `YYYYMMDD-<project>-round-X-input-research-outline.md` |
| Meeting notes | `YYYYMMDD-<project>-round-X-input-meeting-notes.md` |
| Customer material | `YYYYMMDD-<project>-round-X-input-customer-material-<name>.<ext>` |

The first round does not always produce a PRD. If the information is insufficient, output a validation-style `meeting_digest` to identify gaps and the next research focus. If the information is sufficient, generate `<project>-PRD v0.1.md`.

If only a project folder is provided, the skill defaults to detecting the latest PRD, latest validation output, latest research outline, and latest meeting notes, then chooses the appropriate mode from the user's intent: process meeting notes, iterate a PRD, standardize an existing PRD, or review a PRD. It asks for confirmation only when versions, rounds, or candidate files conflict.

### 1. Prepare a customer visit

Use:

```text
Use $bkn-requirement to generate a one-page customer research outline from the following customer background.
```

### 2. Process meeting notes

Use:

```text
Use $bkn-requirement to process this AI meeting note and output this round's research updates, unresolved questions, and PRD impact.
```

You can also provide a project folder or explicit files:

```text
Use $bkn-requirement to process the first-round meeting notes for this project.
Project folder: docs/requirements/prj-guotai-haitong/
Research outline: /path/to/research-outline.md
Meeting notes: /path/to/meeting-notes.md
There is no previous PRD in this round. Output <project>-prd-round-1-validation.md and do not generate a PRD.
```

### 3. Iterate a PRD

Use:

```text
Use $bkn-requirement to update the next PRD version from this research outline, meeting notes and materials, and previous PRD, including the version record.
```

If you only provide the project folder:

```text
Use $bkn-requirement to iterate the PRD from the latest materials in docs/requirements/prj-guotai-haitong/.
Automatically identify the latest PRD, latest research outline, latest meeting notes, and current source manifest.
```

### 4. Standardize an existing PRD or requirement document

If you already have a PRD, BRD, or requirement draft and want to turn it into the standard PRD format, use:

```text
Use $bkn-requirement to turn this existing PRD into a standard PRD.
Input file: /path/to/PRD.md
```

In this case, the skill defaults to outputting `<project>-PRD v0.1.md` or the next suggested version, with a quality summary and scenario-based business follow-up questions. For each core scenario, the PRD body first explains which business objects must be recognized, which business links must be expressed, which judgments / calculations / progressions must happen, and which responsibilities or controls must be governed, before the final `BKN_Creator` handoff summary is produced. It falls back to a validation or review report only when the source material is insufficient.

### 5. Review an existing PRD

Use:

```text
Use $bkn-requirement to assess whether this PRD is ready for BKN_Creator.
```

The skill will identify missing scenario details, unclear rules, data gaps, acceptance gaps, and handoff risks.

### 6. Handoff to `BKN_Creator`

When the PRD is ready, use:

```text
Use $bkn-requirement to generate a BKN_Creator handoff summary.
```

The handoff summary is a Chinese business-readable summary. It is not a machine-readable schema and should not turn the PRD into a modeling file.

The Chinese summary first maps each scenario to:

- Business objects that must be recognized (conceptual model layer).
- Business links that must be expressed (relationship layer).
- Judgments, calculations, or progressions that must happen (dynamic layer).
- Responsibilities, permissions, and traceability that must be controlled (governance layer).
- Business tasks that can be supported by Skill / Agent capabilities.

It then produces the global rollup with business-readable headings:

- Business-confirmed content: confirmed scenarios, objects, rules, systems, and acceptance cases.
- Still modeling candidates: candidates inferred by the AI engineer.
- Items for downstream modeling decisions: modeling questions left for `BKN_Creator`.

## Skill Structure

```text
skills/
  common/
    bkn-methodology.md
  bkn-requirement/
    SKILL.md
    agents/openai.yaml
    assets/
      interview-brief-template.md
      research-plan-template.md
      source-manifest-template.md
      interview-template.md
      requirements-template.md
      scenario-test-case-template.md
      bkn-creator-handoff-template.md
      downstream-agent-card-template.md
    references/
      bkn-methodology.md
      ...
```

## Reading Path

1. Read this file for an overall view of the project’s value, goals, and scope of capabilities.
2. Open `skills/bkn-requirement/SKILL.md` and follow the assets under `skills/bkn-requirement/assets/` for templates and examples.
3. Open `skills/bkn-requirement/references/bkn-methodology.md` for the methodology used by the installed skill. Maintainers can edit `skills/common/bkn-methodology.md` first, then sync it into the skill reference before publishing.

## Support & Contact

- **Issues**: [GitHub Issues](https://github.com/kweaver-ai/kweaver-engineering/issues)
- **License**: [Apache License 2.0](LICENSE)
