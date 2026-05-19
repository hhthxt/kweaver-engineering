[中文](./README.zh.md) | English

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

# KWeaver Engineering

AI engineering capability tools and skill packages for KWeaver BKN projects.

## Skill Overview

This repository provides two Agent Skills for KWeaver BKN projects:

| Skill | Role | Main outputs | Out of scope |
|---|---|---|---|
| `bkn-requirement` | Requirement discovery and PRD structuring | Research outlines, meeting digests, scenario-centered PRDs, `BKN_Creator` handoff summaries | Does not create `.bkn`, bind data, or push platform resources |
| `bkn-ontology-builder` | Ontology modeling scheme generation and refinement | Business-reviewable ontology schemes, Verifier findings, Final Gate reports, implementation feedback refinement notes | Does not create `.bkn`, bind data, or push platform resources |

Recommended flow:

```text
Business material / interview / draft PRD
  -> bkn-requirement
  -> scenario-centered PRD + BKN_Creator handoff summary
  -> optional bkn-ontology-builder
  -> business-reviewable ontology modeling scheme
  -> BKN_Creator
  -> BKN modeling, binding, testing, and validation
  -> optional bkn-ontology-builder refine_mode
  -> implementation-informed scheme revision / delivery archive
```

Both skills use a lightweight Agentic Harness:

```text
Archive / Context -> Generator -> Verifier -> Reviser (if needed) -> Final Gate -> Final Output
```

## Installation

Install a selected skill from this repository with `npx skills`:

```bash
npx skills add https://github.com/kweaver-ai/kweaver-engineering \
  --skill bkn-requirement
```

```bash
npx skills add https://github.com/kweaver-ai/kweaver-engineering \
  --skill bkn-ontology-builder
```

`npx skills` installs the selected skill into the skills location supported by the developer's current AI agent environment. Restart your agent session after installation so the skill list refreshes.

## `bkn-requirement`

`bkn-requirement` is used before formal BKN modeling. It helps AI engineers and business experts turn interviews, meeting notes, draft PRDs, BRDs, process descriptions, and system/data materials into a business-scenario-centered PRD.

### Service Scenarios

- Prepare business expert interviews and material request lists.
- Process interview notes, meeting transcripts, or AI meeting notes.
- Convert rough ideas, PRDs, BRDs, or process documents into standard PRDs.
- Split complex requirements into testable business scenarios.
- Identify missing business rules, data sources, permissions, and acceptance cases.
- Generate follow-up questions, business acceptance cases, and `BKN_Creator` handoff summaries.

### Usage Examples

```text
Use $bkn-requirement to generate a one-page customer research outline from this customer background.
```

```text
Use $bkn-requirement to update the next PRD version from this research outline, meeting notes and materials, and previous PRD.
```

```text
Use $bkn-requirement to generate a BKN_Creator handoff summary.
```

## `bkn-ontology-builder`

`bkn-ontology-builder` turns PRDs, meeting notes, process descriptions, system/data materials, `BKN_Creator` handoff summaries, or existing schemes into a business-reviewable ontology modeling scheme. It is an optional bridge between requirement discovery and formal BKN modeling.

Its `refine_mode` also supports implementation-informed refinement from BKN construction, data binding, Action / Skill implementation, testing, Trace, or Eval feedback. The ontology modeling scheme can evolve as a project deliverable, while the skill still does not create `.bkn` files, bind data views, push networks, or perform platform operations.

### Service Scenarios

- Generate ontology modeling schemes from PRDs, handoff summaries, meeting notes, or business material.
- Refine existing ontology schemes based on business feedback.
- Revise candidate schemes based on Verifier findings.
- Refine schemes from BKN construction, data binding, Action / Skill implementation, testing, Trace, or Eval feedback.
- Compare PRDs and ontology schemes, then output differences, gaps, and strengthening suggestions.

### Usage Examples

```text
Use $bkn-ontology-builder to generate an ontology modeling scheme from this PRD and BKN_Creator handoff summary.
```

```text
Use $bkn-ontology-builder to produce a revised scheme from this existing ontology scheme and Verifier findings.
```

```text
Use $bkn-ontology-builder to revise the ontology modeling scheme from the built .bkn, data binding results, Action/Skill implementation, and test report.
```

## Skill Source And Installation Layout

This repository publishes standard self-contained Agent Skill directories. It also keeps a shared source copy of the BKN methodology under `skills/common/` for cross-skill reuse:

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
  bkn-ontology-builder/
    SKILL.md
    agents/openai.yaml
    assets/
    references/
      bkn-methodology.md
```

Each skill uses its own `references/bkn-methodology.md` at runtime, so `npx skills add ... --skill <skill-name>` can install the selected skill by itself. `skills/common/bkn-methodology.md` is the repository-level source copy; maintainers should sync it into each skill's `references/bkn-methodology.md` before publishing.

## `bkn-methodology.md`

`bkn-methodology.md` is the shared BKN methodology foundation used by both skills. It is not a standalone skill and not a `.bkn` syntax manual. It gives agents a common rule base for deciding object, relation, fact, metric, operator, Action, governance, and Skill / Agent contract boundaries in BKN projects.

It answers questions such as:

- What should become a business object, and what should remain a property, metric, result, state, or rule.
- How relationships should express business paths instead of field joins.
- How to separate queries, calculations, explanation logic, Skill / Agent tasks, and side-effecting Actions.
- How to separate stable facts, runtime state, event records, and audit records.
- How permissions, approvals, Trace, Eval, evidence chains, and human confirmation points enter governance boundaries.

The repository keeps one shared source copy:

```text
skills/common/bkn-methodology.md
```

Each independently installable skill carries its own runtime snapshot:

```text
skills/bkn-requirement/references/bkn-methodology.md
skills/bkn-ontology-builder/references/bkn-methodology.md
```

When maintaining the methodology, edit `skills/common/bkn-methodology.md` first, then run:

```bash
skills/common/sync-common-references.py
```

Before publishing, verify all snapshots are in sync:

```bash
skills/common/sync-common-references.py --check
```

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

For `bkn-ontology-builder`, copy `skills/bkn-ontology-builder/` in the same way.

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

or:

```text
skills/
  bkn-ontology-builder/
```

Keeping `skills/common/bkn-methodology.md` in the same repository is recommended for development, but runtime use does not require it because each distributed skill carries its own methodology snapshot.

When the agent has access to the project workspace, invoke it by name:

```text
Use $bkn-requirement to generate a standard PRD from this interview note.
```

```text
Use $bkn-ontology-builder to generate an ontology modeling scheme from this PRD and handoff summary.
```

## Project Folder And Input Archive

Create one shared folder per customer or project so requirement discovery, ontology modeling, BKN delivery references, presales, and delivery materials do not mix:

```text
docs/prj-<customer-or-project-short-name>/
```

Suggested names:

| Document type | Naming format |
|---|---|
| Research outline | `<project>-round-X-research-outline.md` |
| Meeting memo | `YYYYMMDD-<project>-round-X-meeting-memo.md` |
| Validation output | `<project>-prd-round-X-validation.md` |
| PRD | `<project>-PRD vX.Y.md` |
| Ontology modeling scheme | `<project>-ontology-modeling-scheme vX.Y.md` or `<project>-ontology-modeling-scheme vX.Y-candidate.md` |
| Verifier findings | `<project>-ontology-modeling-scheme vX.Y-verifier-findings.md` |
| Final Gate | `<project>-ontology-modeling-scheme vX.Y-final-gate.md` |
| Implementation feedback refinement note | `<project>-ontology-modeling-scheme vX.Y-implementation-feedback-refine.md` |

Archive each round's input materials under:

```text
docs/prj-<customer-or-project-short-name>/inputs/round-XX/
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

If only a project folder is provided, the skills default to detecting the latest PRD, latest validation output, latest ontology modeling scheme, latest research outline, latest meeting notes, and current source manifest, then choose the appropriate mode from the user's intent. They ask for confirmation only when versions, rounds, or candidate files conflict.

## Skill Structure

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
  bkn-ontology-builder/
    SKILL.md
    agents/openai.yaml
    assets/
    references/
      bkn-methodology.md
```

## Reading Path

1. Read this file for an overall view of the project’s value, goals, and scope of capabilities.
2. For requirement discovery, open `skills/bkn-requirement/SKILL.md` and read that skill's `assets/` and `references/` as needed.
3. For ontology modeling schemes, open `skills/bkn-ontology-builder/SKILL.md` and read that skill's templates and method references as needed.
4. To decide object, relation, metric, operator, Action, governance, and Skill / Agent boundaries, read the relevant skill's `references/bkn-methodology.md`.
5. To maintain shared methodology, edit `skills/common/bkn-methodology.md` first, then sync it into each skill's runtime snapshot.

## Support & Contact

- **Issues**: [GitHub Issues](https://github.com/kweaver-ai/kweaver-engineering/issues)
- **License**: [Apache License 2.0](LICENSE)
