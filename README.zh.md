[English](./README.md) | 中文

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

# KWeaver Engineering

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

## 开源社区阅读路径

1. 先读本文件，从总体上了解项目价值、目标与能力范围。
2. 打开 `skills/bkn-requirement/SKILL.md`，并配合 `skills/bkn-requirement/assets/` 下的模板与示例使用。

## 支持与联系

- **问题反馈**: [GitHub Issues](https://github.com/kweaver-ai/kweaver-engineering/issues)
- **许可证**: [Apache License 2.0](LICENSE)
