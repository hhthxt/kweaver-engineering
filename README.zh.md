[English](./README.md) | 中文

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

# KWeaver Engineering

KWeaver BKN 项目的 AI 工程能力工具与 Skill 包。

## Skill 总览

本仓库当前提供两个面向 KWeaver BKN 项目的 Agent Skill：

| Skill | 定位 | 主要交付物 | 不做什么 |
|---|---|---|---|
| `bkn-requirement` | 需求发现与 PRD 整理 | 调研提纲、会议 digest、场景中心 PRD、`BKN_Creator` 交接摘要 | 不生成 `.bkn`，不绑定数据，不推送平台 |
| `bkn-ontology-builder` | 本体建模方案生成与修订 | 业务可评审的本体建模方案、Verifier findings、Final Gate、实现反馈修订说明 | 不生成 `.bkn`，不绑定数据，不推送平台 |

推荐使用链路：

```text
业务材料 / 访谈 / PRD 草稿
  -> bkn-requirement
  -> 场景中心 PRD + BKN_Creator 交接摘要
  -> 可选 bkn-ontology-builder
  -> 业务可评审的本体建模方案
  -> BKN_Creator
  -> BKN 建模、绑定、测试与验证
  -> 可选 bkn-ontology-builder refine_mode
  -> 实现反馈后的本体建模方案修订 / 交付归档版
```

两个 Skill 都使用轻量 Agentic Harness：

```text
Archive / Context -> Generator -> Verifier -> Reviser（如有必要）-> Final Gate -> Final Output
```

## 安装

使用 `npx skills` 从本仓库安装指定 Skill：

```bash
npx skills add https://github.com/kweaver-ai/kweaver-engineering \
  --skill bkn-requirement
```

```bash
npx skills add https://github.com/kweaver-ai/kweaver-engineering \
  --skill bkn-ontology-builder
```

`npx skills` 会把指定 Skill 安装到开发者当前 AI Agent 环境支持的 skills 位置。安装完成后，重启 Agent 会话，让 Skill 列表刷新。

## `bkn-requirement`

`bkn-requirement` 用于正式 BKN 建模之前的需求发现。它帮助 AI 工程师和业务专家把业务访谈、会议纪要、PRD 草稿、BRD、流程说明、系统材料和数据材料整理成以业务场景为中心的标准 PRD。

### 服务场景

- 准备业务专家访谈和材料索要清单。
- 处理访谈纪要、会议录音转写或 AI 会议纪要。
- 将粗略想法、PRD、BRD 或流程文档整理为标准 PRD。
- 将复杂需求拆成可验收业务场景。
- 识别缺失的业务规则、数据来源、权限要求和验收样例。
- 生成追问清单、业务验收用例和 `BKN_Creator` 交接摘要。

### 使用示例

```text
使用 $bkn-requirement，基于以下客户背景生成一页客户调研提纲。
```

```text
使用 $bkn-requirement，基于本轮调研大纲、会议纪要及相关材料、上一版 PRD，更新新一版 PRD，并生成版本记录。
```

```text
使用 $bkn-requirement，输出 BKN_Creator 交接摘要。
```

## `bkn-ontology-builder`

`bkn-ontology-builder` 用于把 PRD、会议纪要、流程说明、系统/数据材料、`BKN_Creator` 交接摘要或已有方案整理为业务可评审的本体建模方案。它是需求发现和正式 BKN 建模之间的可选桥梁。

`refine_mode` 还支持基于 BKN 构建、数据绑定、Action / Skill 实现、测试、Trace 或 Eval 反馈做实现后反向修订。本体建模方案可以作为项目交付物持续提炼，但本 Skill 仍不创建 `.bkn`、不绑定数据视图、不推送知识网络，也不执行平台操作。

### 服务场景

- 基于 PRD、handoff、会议纪要或业务材料生成本体建模方案。
- 基于已有本体建模方案做业务反馈修订。
- 基于 Verifier findings 定向修订候选方案。
- 基于 BKN 构建、数据绑定、Action / Skill 实现、测试、Trace / Eval 结果做实现反馈修订。
- 对比 PRD 与本体建模方案，输出差异、缺口和补强建议。

### 使用示例

```text
使用 $bkn-ontology-builder，基于这份 PRD 和 BKN_Creator 交接摘要生成本体建模方案。
```

```text
使用 $bkn-ontology-builder，基于已有本体建模方案和 Verifier findings 输出修订版。
```

```text
使用 $bkn-ontology-builder，基于已构建的 .bkn、数据绑定结果、Action/Skill 实现和测试报告，反向修订本体建模方案。
```

## Skill 源码与安装结构

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
  bkn-ontology-builder/
    SKILL.md
    agents/openai.yaml
    assets/
    references/
      bkn-methodology.md
```

每个 Skill 运行时都引用自身的 `references/bkn-methodology.md`，因此 `npx skills add ... --skill <skill-name>` 只安装一个 Skill 目录也可以完整运行。`skills/common/bkn-methodology.md` 是仓库级公共源文件；维护者发布前应把它同步到各 Skill 的 `references/bkn-methodology.md`。

## `bkn-methodology.md`

`bkn-methodology.md` 是两个 Skill 共享的 BKN 方法论基座。它不是独立 Skill，也不是 `.bkn` 语法手册，而是统一 Agent 在 BKN 项目里判断对象、关系、事实、指标、算子、Action、治理和 Skill / Agent 契约边界的参考规则。

它主要回答：

- 什么可以成为业务对象，什么应降级为属性、指标、结果、状态或规则；
- 关系如何表达业务路径，而不是字段 join；
- 查询、计算、解释逻辑、Skill / Agent 任务和有副作用 Action 如何区分；
- 稳定事实、运行状态、事件记录和审计记录如何分离；
- 权限、审批、Trace、Eval、证据链和人工确认点如何进入治理边界。

仓库中保留一份公共源：

```text
skills/common/bkn-methodology.md
```

每个可单独安装的 Skill 都携带自己的运行时快照：

```text
skills/bkn-requirement/references/bkn-methodology.md
skills/bkn-ontology-builder/references/bkn-methodology.md
```

维护时先改 `skills/common/bkn-methodology.md`，再运行：

```bash
skills/common/sync-common-references.py
```

发布前用以下命令确认所有快照一致：

```bash
skills/common/sync-common-references.py --check
```

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

如果安装 `bkn-ontology-builder`，同样复制 `skills/bkn-ontology-builder/`。

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

或：

```text
skills/
  bkn-ontology-builder/
```

开发和维护时建议同时保留 `skills/common/bkn-methodology.md`，但运行时不依赖它，因为每个分发 Skill 自身已经携带方法论快照。

当 Agent 可以访问项目工作区时，可以直接按名称调用：

```text
使用 $bkn-requirement，基于这份访谈纪要输出标准 PRD。
```

```text
使用 $bkn-ontology-builder，基于这份 PRD 和交接摘要生成本体建模方案。
```

## 项目目录与输入归档

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
| 本体建模方案 | `<项目名>-本体建模方案 vX.Y.md` 或 `<项目名>-本体建模方案 vX.Y-candidate.md` |
| Verifier findings | `<项目名>-本体建模方案 vX.Y-verifier-findings.md` |
| Final Gate | `<项目名>-本体建模方案 vX.Y-final-gate.md` |
| 实现反馈修订说明 | `<项目名>-本体建模方案 vX.Y-实现反馈修订说明.md` |

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

如果只提供项目目录，Skill 会默认识别最新 PRD、最新验证输出、最新本体建模方案、最新调研大纲、最新会议纪要和本轮输入源清单，并根据意图选择合适模式。只有版本、轮次或文件选择存在冲突时，才需要用户确认。

## Skill 结构

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

## 开源社区阅读路径

1. 先读本文件，从总体上了解项目价值、目标与能力范围。
2. 需要做需求发现时，打开 `skills/bkn-requirement/SKILL.md`，按需读取该 Skill 的 `assets/` 和 `references/`。
3. 需要生成或修订本体建模方案时，打开 `skills/bkn-ontology-builder/SKILL.md`，按需读取该 Skill 的模板和方法参考。
4. 判断对象、关系、指标、算子、Action、治理和 Skill / Agent 边界时，读取对应 Skill 内的 `references/bkn-methodology.md`。
5. 维护公共方法论时，先编辑 `skills/common/bkn-methodology.md`，再同步到各 Skill 的运行时快照。

## 支持与联系

- **问题反馈**: [GitHub Issues](https://github.com/kweaver-ai/kweaver-engineering/issues)
- **许可证**: [Apache License 2.0](LICENSE)
