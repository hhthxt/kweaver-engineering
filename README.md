# KWeaver Engineering

**English** | [中文](#中文)

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

## License

Apache License 2.0.

---

# 中文

[English](#kweaver-engineering) | **中文**

KWeaver BKN 项目的 AI 工程能力工具与 Skill 包。

## 可用 Skill

### `bkn-requirement`

`bkn-requirement` 是面向 KWeaver BKN 项目的需求发现 Skill。它帮助 AI 工程师和业务专家把业务访谈、会议纪要、PRD 草稿、BRD、流程说明、系统材料和数据材料整理成以业务场景为中心的标准 PRD。

它适用于正式 BKN 建模之前的需求发现阶段。

## 背景

在 BKN 项目里，最难的问题往往不是直接编写模型文件，而是先把业务需求讲清楚：

- 要解决哪个业务场景？
- 谁使用这个能力？
- 当前业务流程是什么？
- 用户期望输入什么、输出什么？
- 哪些业务规则和异常边界必须考虑？
- 涉及哪些业务系统、表单、报表和数据来源？
- 权限、审批、审计边界是什么？
- 业务用户如何验收结果？

`bkn-requirement` 专注于这个上游需求发现工作。它让 PRD 主体保持业务语言表达，并在末尾输出简洁的 `BKN_Creator` 交接摘要，供后续建模使用。

## 服务场景

在以下场景使用 `bkn-requirement`：

- 准备业务专家访谈。
- 处理访谈纪要或会议录音转写。
- 将粗略想法、PRD、BRD 或流程文档整理为标准 PRD。
- 将复杂需求拆成一个个业务场景。
- 识别缺失的业务规则、数据来源、权限要求和验收样例。
- 为 AI 工程师生成追问清单。
- 生成交给 `BKN_Creator` 的交接摘要。

## 与 `BKN_Creator` 的关系

`bkn-requirement` 与 `BKN_Creator` 是前后衔接关系：

```text
业务想法 / 访谈 / PRD 草稿
  -> bkn-requirement
  -> 业务场景中心 PRD
  -> BKN_Creator 交接摘要
  -> BKN_Creator
  -> BKN 建模、绑定、测试与验证
```

`bkn-requirement` 不创建 `.bkn` 文件，不绑定数据视图，不推送知识网络，也不执行平台操作。这些是 `BKN_Creator` 和相关 KWeaver 工程工具的下游职责。

## 安装

### 安装到 Codex / 本地 Agent

克隆仓库：

```bash
git clone https://github.com/kweaver-ai/kweaver-engineering.git
cd kweaver-engineering
```

复制 Skill 到本地 Agent Skills 目录：

```bash
mkdir -p ~/.agents/skills
cp -R skills/bkn-requirement ~/.agents/skills/
```

重启 Agent 会话，让 Skill 列表刷新。

### 在项目中直接使用

也可以将 Skill 放在项目仓库中：

```text
skills/bkn-requirement
```

当 Agent 可以访问项目工作区时，可以直接按名称调用：

```text
使用 $bkn-requirement，基于这份访谈纪要输出标准 PRD。
```

## 如何使用

### 1. 准备业务访谈

使用：

```text
使用 $bkn-requirement，基于 interview-template.md 帮我准备一次业务专家访谈。
```

主要模板：

```text
skills/bkn-requirement/assets/interview-template.md
```

### 2. 将纪要整理成 PRD

使用：

```text
使用 $bkn-requirement，基于这份会议纪要整理业务场景中心 PRD。
```

预期输出包括：

- 业务背景与目标
- 业务用户与职责
- 场景总览
- 场景需求详述
- 业务规则
- 业务系统、表单与数据来源
- 权限与审批要求
- 界面 / 交互期望
- 业务验收用例
- 待确认问题
- `BKN_Creator` 交接摘要

### 3. 评估已有 PRD

使用：

```text
使用 $bkn-requirement，评估这份 PRD 是否可以进入 BKN_Creator。
```

Skill 会识别场景缺口、规则不清、数据缺口、验收缺口和交接风险。

### 4. 交接给 `BKN_Creator`

当 PRD 已准备好时，使用：

```text
使用 $bkn-requirement，输出 BKN_Creator 交接摘要。
```

交接摘要会区分：

- `business_confirmed`：业务已确认的场景、对象、规则、系统和验收用例。
- `candidate_only`：AI 工程师根据 PRD 推导出的建模候选项。
- `needs_bkn_creator_decision`：留给 `BKN_Creator` 判断的建模问题。

## Skill 结构

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

## 不包含的内容

本仓库只发布可安装的 Skill 包。内部设计文档、评审报告、PRD 草稿和项目专用资料不会发布到线上。

## License

Apache License 2.0.
