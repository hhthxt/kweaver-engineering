# 业务验收用例模板

字段名保留英文，便于后续 Eval 或测试流程消费；字段内容使用中文。V0.5 的主表应使用业务输入和业务期望，不要求业务用户理解对象、关系或逻辑属性。

```yaml
business_acceptance_case:
  id:
  scenario:
  type: business_question | analysis_request | decision_recommendation | action_draft | permission_boundary | insufficient_data | evidence_explanation
  user_role:
  user_input:
  expected_business_output:
  required_evidence:
  pass_criteria:
  negative_or_boundary_condition:
```

## 表格形式

| ID | 场景 | 用户输入 | 期望业务输出 | 通过标准 |
|---|---|---|---|---|

## 类型说明

| 类型 | 说明 |
|---|---|
| `business_question` | 业务用户会直接询问的问题。 |
| `analysis_request` | 需要跨系统、跨规则或多步判断的分析任务。 |
| `decision_recommendation` | 需要给出建议、依据和风险边界的任务。 |
| `action_draft` | 只生成草案或建议，不直接执行高风险动作。 |
| `permission_boundary` | 无权限或高风险时应拒绝、转审批或要求确认。 |
| `insufficient_data` | 数据不足、冲突或未对齐时应说明原因。 |
| `evidence_explanation` | 要求输出证据、来源和推理过程。 |

如需技术测试字段，可在 `BKN_Creator` 交接之后追加候选信息：

```yaml
technical_test_candidate:
  required_objects:
  required_relations:
  required_logic_properties:
  allowed_actions:
  trace_requirements:
```
