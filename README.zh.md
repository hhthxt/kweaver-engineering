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

## 需求发现 Harness

`bkn-requirement` V0.7 使用轻量 Agentic Harness，不把生成结果直接当成最终结果：

```text
Archive / Context
  -> Generator
  -> Verifier
  -> Reviser（如有必要）
  -> Final Gate
  -> Final Output
```

- `Generator` 负责按业务场景生成候选 PRD、PRD 迭代或 handoff。
- `Verifier` 负责独立检查候选产物，不直接改文件。
- `Reviser` 只根据 Verifier findings 或用户补充做定向修订。
- `Final Gate` 判定输出是 `pass`、`warn` 还是 `fail`。

Verifier 的检查分为两类：

- 需求规范检查：依据 `SKILL.md`、模板、需求发现方法、质量评分和防跑偏清单。
- BKN 方法论检查：依据 `references/bkn-methodology.md` 和 `references/bkn-requirement-ontology-discovery.md`，检查对象、事实属性、关系、指标、算子、行动、治理和 handoff 边界。

这个 Harness 不要求需求发现阶段执行平台级 Eval / Trace；它只保留必要的输入归档、内部检查 findings、修订摘要和最终门禁结论。若 PRD、PRD 迭代或 handoff 写入项目目录，应同步写入同名 `*-verification-findings.md`，但 findings 不进入 PRD 正文。

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

`bkn-requirement` 不创建 `.bkn` 文件，不绑定数据来源或平台数据视图，不推送知识网络，也不执行平台操作。这些是 `BKN_Creator` 和相关 KWeaver 工程工具的下游职责。

## AI Agent Skills

使用 `npx skills` 从本仓库安装 Skill：

```bash
npx skills add https://github.com/kweaver-ai/kweaver-engineering \
  --skill bkn-requirement
```

`bkn-requirement` — 面向 KWeaver BKN 项目的需求发现 Skill，帮助 AI 工程师把访谈、会议纪要、PRD 草稿、BRD、流程说明和系统/数据材料整理为业务场景中心 PRD，并输出 `BKN_Creator` 交接摘要。参见 `skills/bkn-requirement/SKILL.md`。

`npx skills` 会把指定 Skill 安装到开发者当前 AI Agent 环境支持的 skills 位置。安装完成后，重启 Agent 会话，让 Skill 列表刷新。

### Skill 源码位置

本仓库发布的是一个标准、自包含的 Agent Skill 目录，同时在 `skills/common/` 下保留一份公共源方法论，供多个 Skill 复用和维护：

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

`bkn-requirement` 运行时引用自身的 `references/bkn-methodology.md`，因此 `npx skills add ... --skill bkn-requirement` 只安装这一个 Skill 目录也可以完整运行。`skills/common/bkn-methodology.md` 是仓库级公共源文件；维护者发布前应把它同步到 `skills/bkn-requirement/references/bkn-methodology.md`。

### 手工安装备用方式（高级）

如果目标环境无法使用 `npx skills`，可以克隆仓库后，将 `skills/bkn-requirement/` 复制到该 Agent 官方文档指定的 skills 目录。不同 Agent 的扫描目录不同，请以目标 Agent 的官方说明为准。

```bash
git clone https://github.com/kweaver-ai/kweaver-engineering.git
cd kweaver-engineering
```

期望安装后的结构为：

```text
<skills-root>/
  bkn-requirement/
    SKILL.md
    agents/
    assets/
    references/
      bkn-methodology.md
```

如果安装后的 `bkn-requirement/references/bkn-methodology.md` 缺失，说明安装包不完整，应重新安装或刷新。

Cursor、Codex、OpenClaw 或其他 Agent 是否能自动发现该 Skill，取决于它们是否支持 `SKILL.md` Skill 机制，以及当前 `npx skills` 或 Agent 配置写入的安装目录。

### 开发指引：引用 common 方法论

新增 Skill 如果需要复用 `skills/common/` 下的方法论或公共知识，必须遵守“公共源 + Skill 内分发快照”的结构：

```text
skills/
  common/
    bkn-methodology.md              # 公共源文件，供维护者编辑
  <skill-name>/
    SKILL.md
    references/
      bkn-methodology.md            # 分发快照，供安装后的 Skill 运行时读取
```

规则：

- `SKILL.md` 运行时只引用本 Skill 内部路径，例如 `references/bkn-methodology.md`。
- 不要让已发布 Skill 依赖 `../common/...`，因为 `npx skills add --skill <skill-name>` 可能只安装单个 Skill 目录。
- 维护公共方法论时，先改 `skills/common/<file>.md`，发布前同步到每个需要该文件的 Skill 内部 `references/`。
- 如果多个 Skill 复用同一 common 文件，每个 Skill 都要有自己的分发快照。

每个 Skill 的复制关系登记在：

```text
skills/common/reference-sync.json
```

示例：

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

新增 Skill 复用 common 文件时，只需要在 `copies` 里新增一条登记。

同步所有已登记的分发快照：

```bash
skills/common/sync-common-references.py
```

发布前校验分发快照是否与 common 源一致：

```bash
skills/common/sync-common-references.py --check
```

### 在项目中直接使用

也可以将 Skill 放在项目仓库中：

```text
skills/
  bkn-requirement/
```

开发和维护时建议同时保留 `skills/common/bkn-methodology.md`，但运行时不依赖它，因为 `bkn-requirement` 自身已经携带方法论快照。

当 Agent 可以访问项目工作区时，可以直接按名称调用：

```text
使用 $bkn-requirement，基于这份访谈纪要输出标准 PRD。
```

## 如何使用

### 0. 项目资料目录

每个客户或项目建议建立共享项目目录，避免需求发现、本体建模、BKN 交付参考、售前和交付资料混在一起：

```text
docs/prj-<客户或项目简称>/
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
docs/prj-<客户或项目简称>/inputs/round-XX/
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
项目目录：docs/prj-国泰海通/
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
使用 $bkn-requirement，基于 docs/prj-国泰海通/ 的最新资料迭代 PRD。
请自动识别最新 PRD、最新调研大纲、最新会议纪要和本轮输入源清单。
```

### 4. 整理已有 PRD / 需求文档

如果已有一份 PRD、BRD 或需求草稿，希望整理成标准 PRD，使用：

```text
使用 $bkn-requirement，基于这份已有 PRD 整理为标准 PRD。
输入文件：/path/to/PRD.md
```

这种情况下，Skill 默认输出 `<项目名>-PRD v0.1.md` 或下一建议版本，并在文档中附质量摘要、按场景组织的业务化待确认问题。对每个核心场景，PRD 正文会先说明该场景需要识别哪些业务对象、表达哪些业务联系、完成哪些业务判断 / 计算 / 推进逻辑、控制哪些责任与留痕，再在文末形成 `BKN_Creator` 交接摘要。只有信息不足时，才降级输出验证性结果或评审报告。

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

交接摘要采用中文业务可读表达，不输出机器可读 schema，也不把 PRD 变成建模文件。

中文摘要先按场景收敛：

- 需要识别的业务对象（概念模型层）。
- 需要表达的业务联系（关系层）。
- 需要判断、计算或推进的业务逻辑（动力层）。
- 需要控制的责任、权限与留痕（治理层）。
- 可由 Skill / Agent 支撑的业务任务。

然后再用中文标题做全局归并：

- 业务已确认内容：业务已确认的场景、对象、规则、系统和验收用例。
- 仍属建模候选：AI 工程师根据 PRD 推导出的建模候选项。
- 需下游建模阶段判定的问题：留给 `BKN_Creator` 继续判断的问题。

## Skill 结构

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

## 开源社区阅读路径

1. 先读本文件，从总体上了解项目价值、目标与能力范围。
2. 打开 `skills/bkn-requirement/SKILL.md`，并配合 `skills/bkn-requirement/assets/` 下的模板与示例使用。
3. 判断对象、指标、算子、行动和治理边界时，读取 `skills/bkn-requirement/references/bkn-methodology.md`。维护者可以先编辑 `skills/common/bkn-methodology.md`，发布前同步到该文件。

## 支持与联系

- **问题反馈**: [GitHub Issues](https://github.com/kweaver-ai/kweaver-engineering/issues)
- **许可证**: [Apache License 2.0](LICENSE)
