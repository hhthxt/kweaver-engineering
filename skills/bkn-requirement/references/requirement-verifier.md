# 需求发现 Verifier 规范

## 定位

本文件定义 `bkn-requirement` 的验证标准。Verifier 只做检查和问题定位，不直接改文件。

## 输入

- Generator 生成的候选产物；
- 本轮输入源清单或归档说明；
- `references/anti-drift-checklist.md`；
- `references/bkn-requirement-ontology-discovery.md`；
- `references/bkn-methodology.md`；
- 相关模板和输出结构规则。

## 输出格式

```text
verification_findings:
  hard_stop:
    - 问题：
      证据：
      影响：
      建议修订：
  major:
    - 问题：
      证据：
      影响：
      建议修订：
  minor:
    - 问题：
      证据：
      建议修订：
final_gate:
  verdict: pass | warn | fail
  reason:
  required_revision:
```

## 检查依据

Verifier 的检查依据分为两组。

### 1. 需求规范检查依据

用于判断 PRD 或 handoff 是否像一个可评审的需求产物：

- `SKILL.md` 中的适用场景、输出模式、项目归档、质量门禁；
- `assets/requirements-template.md`、`assets/source-manifest-template.md`、`assets/bkn-creator-handoff-template.md`；
- `references/bkn-requirement-method.md`；
- `references/quality-scoring.md`；
- `references/anti-drift-checklist.md`。

重点检查：场景是否完整、确认状态是否清楚、输入来源是否可追溯、待确认问题是否业务化、验收用例是否可执行、PRD 是否仍然面向业务用户。

### 2. 方法论检查依据

用于判断需求中的 BKN 线索是否符合方法论边界：

- `references/bkn-methodology.md`：统一的 BKN 方法论边界；
- `references/bkn-requirement-ontology-discovery.md`：需求发现阶段的对象、属性、关系、指标、算子、行动、治理裁剪示例。

重点检查：对象是否稳定、字段是否被误升为对象、结果类内容是否被默认对象化、关系是否有业务语义、指标是否有口径、算子是否有输入规则输出、行动是否真的改变或影响对象、工具是否被误当成业务行动。

注意：`references/bkn-methodology.md` 中关于 Trace / Eval 的内容属于下游 Agent、Action、平台运行和治理设计要求。`bkn-requirement` 阶段只检查是否提出了可验收、可追溯来源、可留痕或需治理的业务要求，不执行平台级 Eval / Trace，也不要求 PRD 记录 Agent 运行轨迹。

## 分级标准

| 级别 | 判定 | 处理 |
|---|---|---|
| `hard_stop` | 不得声称 PRD Ready、handoff Ready 或可进入 BKN_Creator | 必须修订 |
| `major` | 影响业务评审、下游建模质量或验收可执行性 | 原则上修订 |
| `minor` | 表达、可读性、局部完整性问题 | 可修订或记录 |

## Hard Stop

出现以下任一情况，必须判定为 hard stop：

- 输入未归档，也未说明无法归档的原因；
- 输出模式与用户意图不匹配；
- PRD 正文与待确认事项冲突，却写成已确认；
- `业务已确认内容` 混入“待确认 / 未确认 / 待对齐 / 是否 / 范围待定 / 范围待确认 / 候选”等信号；
- P0 / P1 场景缺少业务目标、触发、输入、输出、关键决策点或操作闭环；
- `BKN_Creator` 交接摘要只列对象名、关系名或逻辑名，没有说明业务含义；
- 关系层核心名词未在概念模型层说明；
- 指标没有口径，算子没有输入 / 规则 / 输出 / 边界，行动没有说明会改变或影响什么；
- 把结果类内容默认对象化，例如满足方案行、缺口行、报表行、看板指标；
- 输出 YAML / JSON / 机器可读 schema 作为 PRD 正文或 handoff 正文。

## Major Findings

以下通常判定为 major：

- 待确认问题未按场景组织；
- 待确认问题没有说明问谁、为什么问、不确认风险和建议问法；
- 业务系统、表单、数据来源、事实来源或刷新频率缺失；
- 验收用例缺少边界、权限拒绝、数据不足或证据解释类用例；
- 场景收敛没有区分事实属性、关系、指标、算子、行动和治理；
- 采购、拆料、写回、通知等高影响动作没有治理边界；
- 需求成熟度与当前缺口不一致；
- `仍属建模候选` 与 `需下游建模阶段判定的问题` 混在一起。

## Minor Findings

以下通常判定为 minor：

- 章节标题不完全一致，但不影响理解；
- 局部表达过于简略，但主线完整；
- 少量术语可进一步业务化；
- 示例不足，但已给出明确补充方向。

## 检查维度

### 1. 业务完整性

检查：

- 背景、痛点、目标是否清楚；
- 用户角色和职责是否明确；
- 场景是否按业务能力拆分；
- 每个核心场景是否有触发、当前流程、目标流程、输入、输出、异常和验收标准。

### 2. 确认状态

检查：

- 已确认、候选、待确认是否分开；
- 是否存在“句子前半段是结论，后半段是待确认”；
- 是否把 AI 工程推断写成业务确认。

### 3. BKN 方法论边界

检查：

- 对象是否具备稳定身份、生命周期、责任、关系或管理动作；
- 编码、状态、数量、日期、类型、原因是否优先作为事实属性或枚举；
- 关系是否连接两个已说明对象，并表达业务含义；
- 指标是否有统一口径；
- 算子是否说明输入、规则、输出和边界；
- 行动是否改变对象、影响对象或触发外部系统；
- 治理是否说明责任、权限、审批、留痕或拒绝自动化边界；
- 工具 / API / MCP 是否只作为执行绑定线索，没有替代业务行动、业务规则或业务验收标准。

### 4. Harness 工程完整性

检查：

- 是否能识别 Generator 候选产物，而不是直接把候选当最终结果；
- Verifier findings 是否有证据、影响和建议修订；
- Reviser 是否只基于 findings 或用户补充修订；
- 是否保留修订摘要，避免重新自由生成；
- Final Gate 是否明确给出 pass / warn / fail；
- warn / fail 是否说明剩余问题和下一轮追问。

### 5. 交接摘要质量

检查：

- 是否按场景逐项说明对象、关系、动力层、治理层和 Skill / Agent 任务；
- 是否说明“是什么、为什么需要、怎么判断 / 计算、谁负责、输出什么”；
- 是否避免把正文业务意义压缩回孤立名词列表；
- 全局归并是否分为 `业务已确认内容`、`仍属建模候选`、`需下游建模阶段判定的问题`。

### 6. 反技术化

检查：

- PRD 主体是否使用业务语言；
- 技术字段、接口、主键、关系基数、data_view、ActionType 等是否被转译；
- 是否把 PRD 写成 `.bkn` 草案或机器 schema。

## Final Gate 判定

| verdict | 条件 |
|---|---|
| `pass` | 无 hard stop，major 已处理或有明确业务可接受解释 |
| `warn` | 无 hard stop，但仍有关键业务待确认，文档只能标为 Draft / Candidate |
| `fail` | 存在 hard stop，或修订两轮后仍未清除 |

Verifier 不负责修订，但必须给出可执行的修订建议。
