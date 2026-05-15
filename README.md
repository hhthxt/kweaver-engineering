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

`bkn-requirement` does not create `.bkn` files, bind data views, push networks, or execute platform operations. Those are downstream responsibilities of `BKN_Creator` and related KWeaver engineering tools.

## AI Agent Skills

Install the skill from this repository with `npx skills`:

```bash
npx skills add https://github.com/kweaver-ai/kweaver-engineering \
  --skill bkn-requirement
```

`bkn-requirement` — a requirement discovery skill for KWeaver BKN projects. It helps AI engineers turn interviews, meeting notes, draft PRDs, BRDs, process descriptions, and system/data materials into a business-scenario-centered PRD, then produce a `BKN_Creator` handoff summary. See `skills/bkn-requirement/SKILL.md`.

`npx skills` installs the selected skill into the skills location supported by the developer's current AI agent environment. Restart your agent session after installation so the skill list refreshes.

### Skill Source

This repository publishes a standard Agent Skill directory:

```text
skills/bkn-requirement/
  SKILL.md
  agents/openai.yaml
  assets/
  references/
```

Any agent that supports `SKILL.md`-based skills can install this directory. Use the `npx skills add` command above as the default installation path.

### Manual Fallback (Advanced)

If the target environment cannot use `npx skills`, clone the repository and copy `skills/bkn-requirement/` into the skills directory documented by that agent. Different agents scan different locations, so follow the target agent's official documentation.

```bash
git clone https://github.com/kweaver-ai/kweaver-engineering.git
cd kweaver-engineering
```

Cursor, Codex, OpenClaw, and other agents can discover this skill only if they support `SKILL.md`-based skills and scan the directory written by `npx skills` or by the agent configuration.

### Use directly from a project

You can also keep the skill in a project repository under:

```text
skills/bkn-requirement
```

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

The first round does not always produce a PRD. If the information is insufficient, output a validation-style `meeting_digest` to identify gaps and the next research focus. If the information is sufficient, generate `<project>-PRD v0.1.md`.

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

### 3. Iterate a PRD

Use:

```text
Use $bkn-requirement to update the next PRD version from this research outline, meeting notes and materials, and previous PRD, including the version record.
```

### 4. Review an existing PRD

Use:

```text
Use $bkn-requirement to assess whether this PRD is ready for BKN_Creator.
```

The skill will identify missing scenario details, unclear rules, data gaps, acceptance gaps, and handoff risks.

### 5. Handoff to `BKN_Creator`

When the PRD is ready, use:

```text
Use $bkn-requirement to generate a BKN_Creator handoff summary.
```

The handoff summary separates:

- `business_confirmed`: business-confirmed scenarios, objects, rules, systems, and acceptance cases.
- `candidate_only`: modeling candidates inferred by the AI engineer.
- `needs_bkn_creator_decision`: modeling decisions left for `BKN_Creator`.

## Skill Structure

```text
skills/bkn-requirement/
  SKILL.md
  agents/openai.yaml
  assets/
    interview-brief-template.md
    research-plan-template.md
    interview-template.md
    requirements-template.md
    scenario-test-case-template.md
    bkn-creator-handoff-template.md
    downstream-agent-card-template.md
  references/
    ...
```

## Reading Path

1. Read this file for an overall view of the project’s value, goals, and scope of capabilities.
2. Open `skills/bkn-requirement/SKILL.md` and follow the assets under `skills/bkn-requirement/assets/` for templates and examples.

## Support & Contact

- **Issues**: [GitHub Issues](https://github.com/kweaver-ai/kweaver-engineering/issues)
- **License**: [Apache License 2.0](LICENSE)
