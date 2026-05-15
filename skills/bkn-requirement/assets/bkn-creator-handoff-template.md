# BKN_Creator 交接模板

字段名保留英文，便于后续 `bkn-creator` 消费；字段内容和说明使用中文。

V0.5 要求明确区分业务已确认内容、建模候选内容和需要 `BKN_Creator` 判定的内容。不要把候选对象、关系、逻辑属性或 Action 写成业务已确认事实。

```yaml
bkn_creator_handoff:
  schema_version: bkn-requirement.v0.5
  source_prd:
  handoff_route: hold | interview | extract_after_prd_refinement | extract_after_scene_split | create_after_business_confirmation | update
  requirement_maturity: R0 | R1 | R2 | R3 | R4
  quality_score:
  business_domain:
  use_case_name:
  candidate_network_name:
  business_confirmed:
    business_scenarios:
    business_objects:
    business_rules:
    business_systems:
    business_acceptance_cases:
  candidate_only:
    candidate_objects:
    candidate_relations:
    candidate_logic_properties:
    candidate_actions:
    candidate_risk_types:
    candidate_skills:
    data_view_candidates:
    external_writeback_systems:
  needs_bkn_creator_decision:
  critical_gaps:
  requires_business_confirmation:
  schema_validation:
    missing_required_fields:
    inconsistent_fields:
    validation_notes:
  suggested_next_step:
```

## 字段说明

| 字段 | 说明 |
|---|---|
| `schema_version` | 输出结构版本，V0.5 固定为 `bkn-requirement.v0.5`。 |
| `handoff_route` | 建议 `BKN_Creator` 下游路线。PRD 未完成时应优先 `interview`、`extract_after_prd_refinement` 或 `extract_after_scene_split`。 |
| `business_confirmed` | 已能被业务专家直接确认的场景、对象、规则、系统和验收用例，使用业务语言。 |
| `candidate_only` | AI 工程师根据 PRD 推导出的 BKN 候选项，仍需 `BKN_Creator` 判断。 |
| `needs_bkn_creator_decision` | 明确交给 `BKN_Creator` 决定的建模问题，如对象边界、关系对象、逻辑属性挂载、Action 执行模式。 |
| `critical_gaps` | 阻碍进入下一成熟度的关键缺口。 |
| `requires_business_confirmation` | 仍需业务专家确认的事项。 |
| `schema_validation` | 对 handoff 必填字段、正文一致性和缺失项的校验结果。 |
| `suggested_next_step` | 建议下一步。 |
