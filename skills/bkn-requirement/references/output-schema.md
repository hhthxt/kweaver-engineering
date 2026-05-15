# 输出 Schema

用于 V0.5 结构化输出。完整 PRD 可按需要输出：

- `research_plan`：会前调研准备和客户现场短提纲。
- `meeting_digest`：会议纪要结构化结果。
- `prd_revision`：PRD 迭代更新摘要和版本记录。
- `requirement_schema`：业务场景中心的结构化需求索引。
- `quality_assessment`：PRD 质量评分与成熟度。
- `bkn_creator_handoff`：交给 `bkn-creator` 的下游交接信息。

字段名保留英文，便于后续程序消费；字段说明和字段内容使用中文。

## 路由字段约定

V0.5 区分两类路线：

| 字段 | 用途 | 枚举 |
|---|---|---|
| `quality_assessment.readiness_decision.quality_route` | 判断 PRD 质量和下一步需求工作 | `hold`、`research_plan`、`interview`、`prd_iteration`、`prd_refinement`、`business_review`、`bkn_creator_handoff` |
| `bkn_creator_handoff.handoff_route` | 判断交给 `BKN_Creator` 后的下游动作 | `hold`、`interview`、`extract_after_prd_refinement`、`extract_after_scene_split`、`create_after_business_confirmation`、`update` |

V0.5 输出模式枚举：

```yaml
output_mode: intake_mode | research_plan_mode | meeting_digest_mode | prd_iteration_mode | prd_mode | review_mode | handoff_mode
```

映射建议：

| quality_route | handoff_route |
|---|---|
| `hold` | `hold` |
| `research_plan` | `interview` |
| `interview` | `interview` |
| `prd_iteration` | `extract_after_prd_refinement` |
| `prd_refinement` | `extract_after_prd_refinement` 或 `extract_after_scene_split` |
| `business_review` | `extract_after_scene_split` |
| `bkn_creator_handoff` | `create_after_business_confirmation` 或 `update` |

## research_plan

```yaml
research_plan:
  schema_version: bkn-requirement.v0.5
  customer:
    name:
    industry:
    department_or_team:
    interview_target_roles:
  research_goal:
  known_background:
  customer_brief_questions:
    - topic:
      question:
      purpose:
  suggested_participants:
  materials_to_request:
  expected_post_meeting_outputs:
```

## meeting_digest

```yaml
meeting_digest:
  schema_version: bkn-requirement.v0.5
  meeting:
    date:
    participants:
    source_materials:
    research_outline:
    previous_prd:
  goal_alignment:
    planned_questions:
    confirmed_in_meeting:
    not_confirmed:
  confirmed_facts:
  assumptions:
  conflicts:
  business_scenarios:
  business_rules:
  systems_forms_and_data:
  acceptance_examples:
  prd_impact:
    add:
    update:
    remove:
    affected_sections:
  unresolved_questions:
  next_research_focus:
```

## prd_revision

```yaml
prd_revision:
  schema_version: bkn-requirement.v0.5
  inputs:
    research_outline:
    meeting_notes_and_materials:
    previous_prd:
  revision:
    previous_version:
    new_version:
    document_status: draft | business_review | confirmed | handoff_ready
    revision_summary:
    added_confirmed_facts:
    corrected_facts:
    removed_or_out_of_scope:
    affected_sections:
    unresolved_questions:
    next_research_focus:
  change_log_entry:
    version:
    date:
    input_sources:
    major_changes:
    still_unconfirmed:
```

## requirement_schema

`requirement_schema` 用于把正文 PRD 固化为机器可读结构。它不替代正文，也不要求业务用户理解 BKN。

```yaml
requirement_schema:
  schema_version: bkn-requirement.v0.5
  document:
    title:
    version:
    previous_version:
    source_inputs:
    output_mode: intake_mode | research_plan_mode | meeting_digest_mode | prd_iteration_mode | prd_mode | review_mode | handoff_mode
    status: draft | business_review | confirmed | handoff_ready
    current_iteration_summary:
  business_context:
    domain:
    use_case_name:
    business_background:
    business_goals:
    success_metrics:
    in_scope:
    out_of_scope:
    assumptions:
  business_users:
    - role:
      responsibilities:
      frequent_questions_or_tasks:
      permission_boundary:
  business_scenarios:
    - id:
      name:
      primary_users:
      business_goal:
      priority: P0 | P1 | P2
      maturity: R0 | R1 | R2 | R3 | R4
      trigger:
      current_workflow:
      target_workflow:
      inputs:
      outputs:
      business_rules:
      exception_boundaries:
      human_confirmation_points:
      interface_expectations:
      acceptance_criteria:
  cross_scenario_rules:
    - id:
      name:
      business_description:
      affected_scenarios:
      unresolved_points:
  systems_forms_and_data:
    - name:
      type: business_system | form | data_source | report | external_service
      business_purpose:
      source_of_truth: true | false | unknown
      key_fields_or_information:
      owner:
      refresh_frequency:
      access_restriction:
      quality_risks:
  permissions_governance:
    - capability_or_operation:
      allowed_roles:
      control_requirements:
      approval_required: true | false | unknown
      audit_requirement:
  interface_expectations:
    - page_or_entry:
      key_interactions:
      expected_outputs:
  business_acceptance_cases:
    - id:
      scenario:
      user_input:
      expected_business_output:
      pass_criteria:
      required_evidence:
  unresolved_questions:
    - id:
      question:
      ask_to:
      reason_to_ask:
      risk_if_unconfirmed:
      suggested_wording:
      priority: P0 | P1 | P2
```

## quality_assessment

评分细则见 `references/quality-scoring.md`。

```yaml
quality_assessment:
  schema_version: bkn-requirement.v0.5
  requirement_maturity: R0 | R1 | R2 | R3 | R4
  total_score: 0-100
  readiness_decision:
    quality_route: hold | research_plan | interview | prd_iteration | prd_refinement | business_review | bkn_creator_handoff
    mapped_handoff_route: hold | interview | extract_after_prd_refinement | extract_after_scene_split | create_after_business_confirmation | update
    decision_reason:
  dimension_scores:
    business_goal_clarity:
      score: 0-100
      evidence:
      gaps:
      next_actions:
    scenario_completeness:
      score: 0-100
      evidence:
      gaps:
      next_actions:
    workflow_and_decision_clarity:
      score: 0-100
      evidence:
      gaps:
      next_actions:
    business_rule_clarity:
      score: 0-100
      evidence:
      gaps:
      next_actions:
    system_data_readiness:
      score: 0-100
      evidence:
      gaps:
      next_actions:
    governance_and_permission_readiness:
      score: 0-100
      evidence:
      gaps:
      next_actions:
    acceptance_case_coverage:
      score: 0-100
      evidence:
      gaps:
      next_actions:
    bkn_creator_handoff_quality:
      score: 0-100
      evidence:
      gaps:
      next_actions:
  critical_gaps:
    - gap:
      impact:
      owner:
      priority: P0 | P1 | P2
  promotion_criteria:
    next_maturity:
    required_evidence:
```

## bkn_creator_handoff

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

## 业务验收用例

```yaml
business_acceptance_case:
  id:
  scenario:
  user_role:
  user_input:
  expected_business_output:
  required_evidence:
  pass_criteria:
  negative_or_boundary_condition:
```

如果确实需要给 `bkn-creator` 或 `bkn-test` 生成技术测试，可在 handoff 后附加候选测试信息，但不要替代业务验收用例。
