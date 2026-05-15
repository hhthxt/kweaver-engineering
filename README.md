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

## Installation

### Install for Codex / local agent usage

Clone this repository:

```bash
git clone https://github.com/kweaver-ai/kweaver-engineering.git
cd kweaver-engineering
```

Copy the skill into your local agent skills directory:

```bash
mkdir -p ~/.agents/skills
cp -R skills/bkn-requirement ~/.agents/skills/
```

Restart your agent session so the skill list refreshes.

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

### 1. Prepare an interview

Use:

```text
Use $bkn-requirement and interview-template.md to prepare a business expert interview.
```

Main template:

```text
skills/bkn-requirement/assets/interview-template.md
```

### 2. Convert notes into a PRD

Use:

```text
Use $bkn-requirement to convert this meeting note into a business-scenario-centered PRD.
```

Expected output:

- Business background and goals
- Business users and responsibilities
- Scenario overview
- Scenario details
- Business rules
- Systems, forms, and data sources
- Permission and approval requirements
- Interface expectations
- Business acceptance cases
- Follow-up questions
- `BKN_Creator` handoff summary

### 3. Review an existing PRD

Use:

```text
Use $bkn-requirement to assess whether this PRD is ready for BKN_Creator.
```

The skill will identify missing scenario details, unclear rules, data gaps, acceptance gaps, and handoff risks.

### 4. Handoff to `BKN_Creator`

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
    interview-template.md
    requirements-template.md
    scenario-test-case-template.md
    bkn-creator-handoff-template.md
    downstream-agent-card-template.md
  references/
    ...
```

## What Is Not Included

This repository publishes the installable skill package only. Internal design notes, review reports, draft PRDs, and project-specific documents are not included.

## Reading Path

1. Read this file for an overall view of the project’s value, goals, and scope of capabilities.
2. Open `skills/bkn-requirement/SKILL.md` and follow the assets under `skills/bkn-requirement/assets/` for templates and examples.

## Support & Contact

- **Issues**: [GitHub Issues](https://github.com/kweaver-ai/kweaver-engineering/issues)
- **License**: [Apache License 2.0](LICENSE)
