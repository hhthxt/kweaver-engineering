# 质量评分规则

用于 V0.5 的 `quality_assessment` 输出。评分目的是判断 PRD 是否足以让业务专家评审、让 AI 工程师追问、并让 `BKN_Creator` 接收，不是给 BKN 模型打分。

## 总分计算

总分 100 分，按以下权重加权：

| 维度 | 权重 | 评分目标 |
|---|---:|---|
| `business_goal_clarity` | 10 | 业务背景、目标、成功指标、范围边界是否清楚。 |
| `scenario_completeness` | 20 | 是否拆成可验收业务场景，每个场景有用户、触发、输入、输出和验收标准。 |
| `workflow_and_decision_clarity` | 15 | 当前流程、目标流程、决策点、人机协同和人工确认点是否清楚。 |
| `business_rule_clarity` | 15 | 业务规则、判断标准、异常边界和可配置项是否明确。 |
| `system_data_readiness` | 15 | 业务系统、表单、数据源、事实来源、字段口径、刷新频率和质量风险是否明确。 |
| `governance_and_permission_readiness` | 10 | 权限、审批、审计、敏感数据、高风险动作和拒绝边界是否明确。 |
| `acceptance_case_coverage` | 10 | 业务验收用例是否覆盖典型问题、分析、决策、权限拒绝、数据不足和证据解释。 |
| `bkn_creator_handoff_quality` | 5 | 交接摘要是否区分业务已确认、候选建模项和需下游判定的问题。 |

总分计算公式：

```text
total_score =
  business_goal_clarity * 0.10 +
  scenario_completeness * 0.20 +
  workflow_and_decision_clarity * 0.15 +
  business_rule_clarity * 0.15 +
  system_data_readiness * 0.15 +
  governance_and_permission_readiness * 0.10 +
  acceptance_case_coverage * 0.10 +
  bkn_creator_handoff_quality * 0.05
```

## 单项评分口径

每个维度使用 0 到 100 分：

| 分数段 | 含义 |
|---:|---|
| 0-20 | 信息基本缺失，无法评审。 |
| 21-40 | 有零散线索，但不能形成稳定需求。 |
| 41-60 | 可形成候选需求，缺关键确认。 |
| 61-80 | 业务 PRD 基本可评审，仍有若干待确认项。 |
| 81-95 | 可进入实现准备，仅有少量边界问题。 |
| 96-100 | 证据、口径、样例、权限和验收均已确认。 |

评分必须给出 `evidence`、`gaps` 和 `next_actions`。不要只给数字。

## 成熟度映射

成熟度不是机械等于总分，需要同时满足硬性条件。

| 成熟度 | 总分参考 | 硬性条件 | 推荐路线 |
|---|---:|---|---|
| R0 Idea | 0-25 | 只有想法，缺用户、目标或场景。 | `hold` |
| R1 Use Case Brief | 26-45 | 客户、用户、目标或场景大致明确，但缺流程、规则、数据和验收。 | `research_plan` / `interview` |
| R2 PRD Candidate | 46-65 | 已有场景和规则候选，但关键口径、系统数据或验收样例待确认。 | `prd_iteration` / `prd_refinement` |
| R3 PRD Ready | 66-82 | 业务场景、流程、规则、系统数据和验收用例基本可评审。 | `business_review` |
| R4 Implementation Ready | 83-100 | 字段、样例、权限、治理、交互、验收标准和下游交接均已确认。 | `bkn_creator_handoff` |

如果存在以下情况，即使总分较高，也不能评为 R4：

- 缺少业务验收样例或标准答案；
- 核心业务规则、判断标准或异常边界未确认；
- 核心业务系统、表单、字段口径或样例数据缺失；
- 高风险操作的权限、审批或失败处理未确认；
- 界面 / 交互期望缺失，业务用户无法判断如何使用；
- `bkn_creator_handoff` 未区分 `business_confirmed`、`candidate_only`、`needs_bkn_creator_decision`。

## 推荐路线规则

V0.5 区分两类路线：

- `quality_route`：PRD 质量路线，用在 `quality_assessment.readiness_decision`。
- `handoff_route`：BKN_Creator 下游路线，用在 `bkn_creator_handoff`。

### quality_route

| 推荐路线 | 触发条件 |
|---|---|
| `hold` | 需求只有想法，缺业务目标或决策场景。 |
| `research_plan` | 已有客户背景和拜访目标，但缺完整流程和规则，适合先生成调研提纲。 |
| `interview` | 需求方向存在，但缺关键业务规则、流程或角色确认。 |
| `prd_iteration` | 有上一版 PRD 和本轮会议材料，需要生成新版本。 |
| `prd_refinement` | 输入来自 PRD、会议纪要或材料汇总，已能整理 PRD，但需要补场景、规则、数据或验收。 |
| `business_review` | PRD 基本完整，适合组织业务专家评审。 |
| `bkn_creator_handoff` | PRD 已确认，能清晰交给 `BKN_Creator` 做建模抽取和后续验证。 |

### handoff_route 映射

| quality_route | 默认 handoff_route | 说明 |
|---|---|---|
| `hold` | `hold` | 暂不交接。 |
| `research_plan` | `interview` | 先调研，不交接。 |
| `interview` | `interview` | 继续访谈。 |
| `prd_iteration` | `extract_after_prd_refinement` | 先完成 PRD 版本更新和缺口确认。 |
| `prd_refinement` | `extract_after_prd_refinement` | PRD 可抽取候选项，但需先补业务缺口。 |
| `business_review` | `extract_after_scene_split` | 场景基本清晰，可交给 `BKN_Creator` 做场景化抽取。 |
| `bkn_creator_handoff` | `create_after_business_confirmation` | 业务确认后可进入建模创建；已有 BKN 时可选 `update`。 |

## 必须识别的关键缺口

输出 `critical_gaps` 时优先识别以下问题：

- 业务目标、用户角色、成功指标或范围边界缺失；
- 场景未拆清楚，只有功能列表或建模清单；
- 当前流程、目标流程、决策点、人工确认点缺失；
- 业务规则、判断标准、异常边界、可配置项缺失；
- 业务系统、表单、数据源、事实来源、字段口径、刷新频率或质量风险缺失；
- 权限、审批、审计、失败处理或拒绝执行边界缺失；
- 业务验收用例未覆盖典型、边界、权限拒绝、数据不足和证据解释；
- handoff 字段不完整或把候选建模项误写成业务确认项。

## 输出要求

完整质量评分必须包含：

- 总分和成熟度；
- `quality_route`、映射后的 `handoff_route` 和理由；
- 8 个分项评分；
- 每个分项的证据、缺口和下一步动作；
- P0/P1/P2 关键缺口；
- 晋级到下一成熟度需要补充的证据。
