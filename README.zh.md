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

## AI Agent Skills

使用 `npx skills` 从本仓库安装 Skill：

```bash
npx skills add https://github.com/kweaver-ai/kweaver-engineering \
  --skill bkn-requirement
```

`bkn-requirement` — 面向 KWeaver BKN 项目的需求发现 Skill，帮助 AI 工程师把访谈、会议纪要、PRD 草稿、BRD、流程说明和系统/数据材料整理为业务场景中心 PRD，并输出 `BKN_Creator` 交接摘要。参见 `skills/bkn-requirement/SKILL.md`。

`npx skills` 会把指定 Skill 安装到开发者当前 AI Agent 环境支持的 skills 位置。安装完成后，重启 Agent 会话，让 Skill 列表刷新。

### Skill 源码位置

本仓库发布的是一个标准 Agent Skill 目录：

```text
skills/bkn-requirement/
  SKILL.md
  agents/openai.yaml
  assets/
  references/
```

只要目标 Agent 支持以 `SKILL.md` 为入口的 Skill 机制，就可以安装这个目录。推荐使用上面的 `npx skills add` 命令安装。

### 手工安装备用方式（高级）

如果目标环境无法使用 `npx skills`，可以克隆仓库后，将 `skills/bkn-requirement/` 复制到该 Agent 官方文档指定的 skills 目录。不同 Agent 的扫描目录不同，请以目标 Agent 的官方说明为准。

```bash
git clone https://github.com/kweaver-ai/kweaver-engineering.git
cd kweaver-engineering
```

Cursor、Codex、OpenClaw 或其他 Agent 是否能自动发现该 Skill，取决于它们是否支持 `SKILL.md` Skill 机制，以及当前 `npx skills` 或 Agent 配置写入的安装目录。

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

### 0. 项目资料目录

每个客户或项目建议建立独立目录，避免售前、交付和开发资料混在一起：

```text
docs/requirements/prj-<客户或项目简称>/
```

命名建议：

| 文档类型 | 命名格式 |
|---|---|
| 调研大纲 | `<项目名>-第X轮调研大纲.md` |
| 调研备忘 | `YYYYMMDD-<项目名>-第X轮现场交流调研备忘.md` |
| 验证输出 | `<项目名>-prd-第X轮验证输出.md` |
| PRD | `<项目名>-PRD vX.Y.md` |

每一轮输入材料建议归档到：

```text
docs/requirements/prj-<客户或项目简称>/inputs/round-XX/
```

如果用户指定的输入文件不在项目文件夹内，Skill 必须先复制一份到本轮 `inputs/round-XX/`，不移动原始文件；如果输入文件已经在项目文件夹内，可以不复制，但应生成或更新 `source-manifest.md` 记录本轮输入来源。

`source-manifest.md` 只能记录真实发生的归档动作。凡标记为“已复制”的归档路径必须真实存在；如果复制失败或路径不可访问，必须在清单和最终输出中说明，不得写成“已复制”。

推荐输入文件命名：

| 输入类型 | 命名格式 |
|---|---|
| 调研大纲 | `YYYYMMDD-<项目名>-第X轮-input-调研大纲.md` |
| 会议纪要 | `YYYYMMDD-<项目名>-第X轮-input-会议纪要.md` |
| 客户材料 | `YYYYMMDD-<项目名>-第X轮-input-客户材料-<材料名>.<ext>` |

第一轮调研后不一定直接生成 PRD。如果信息不足，先输出验证性 `meeting_digest`，用于判断缺口和下一轮调研重点；如果信息足够，再生成 `<项目名>-PRD v0.1.md`。

如果只提供项目目录，Skill 会默认识别最新 PRD、最新验证输出、最新调研大纲和最新会议纪要，并根据意图选择“处理会议纪要”“迭代 PRD”“整理为标准 PRD”或“评估 PRD”。只有版本、轮次或文件选择存在冲突时，才需要用户确认。

### 1. 准备客户拜访

使用：

```text
使用 $bkn-requirement，基于以下客户背景生成一页客户调研提纲。
```

### 2. 处理会议纪要

使用：

```text
使用 $bkn-requirement，基于这份豆包会议纪要，输出本轮调研更新、待确认问题和 PRD 影响。
```

也可以只提供项目目录或指定本轮输入文件：

```text
使用 $bkn-requirement，处理这个项目的第一轮会议纪要。
项目目录：docs/requirements/prj-国泰海通/
本轮调研大纲：/path/to/调研大纲.md
本轮会议纪要：/path/to/会议纪要.md
本轮没有上一版 PRD，请输出 <项目名>-prd-第1轮验证输出.md，不要生成 PRD。
```

### 3. 迭代 PRD

使用：

```text
使用 $bkn-requirement，基于本轮调研大纲、会议纪要及相关材料、上一版 PRD，更新新一版 PRD，并生成版本记录。
```

如果只给项目目录：

```text
使用 $bkn-requirement，基于 docs/requirements/prj-国泰海通/ 的最新资料迭代 PRD。
请自动识别最新 PRD、最新调研大纲、最新会议纪要和本轮输入源清单。
```

### 4. 整理已有 PRD / 需求文档

如果已有一份 PRD、BRD 或需求草稿，希望整理成标准 PRD，使用：

```text
使用 $bkn-requirement，基于这份已有 PRD 整理为标准 PRD。
输入文件：/path/to/PRD.md
```

这种情况下，Skill 默认输出 `<项目名>-PRD v0.1.md` 或下一建议版本，并在文档中附质量摘要、待确认问题和 `BKN_Creator` 交接摘要。只有信息不足时，才降级输出验证性结果或评审报告。

### 5. 评估已有 PRD

使用：

```text
使用 $bkn-requirement，评估这份 PRD 是否可以进入 BKN_Creator。
```

Skill 会识别场景缺口、规则不清、数据缺口、验收缺口和交接风险。

### 6. 交接给 `BKN_Creator`

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
    interview-brief-template.md
    research-plan-template.md
    source-manifest-template.md
    interview-template.md
    requirements-template.md
    scenario-test-case-template.md
    bkn-creator-handoff-template.md
    downstream-agent-card-template.md
  references/
    ...
```

## 开源社区阅读路径

1. 先读本文件，从总体上了解项目价值、目标与能力范围。
2. 打开 `skills/bkn-requirement/SKILL.md`，并配合 `skills/bkn-requirement/assets/` 下的模板与示例使用。

## 支持与联系

- **问题反馈**: [GitHub Issues](https://github.com/kweaver-ai/kweaver-engineering/issues)
- **许可证**: [Apache License 2.0](LICENSE)
