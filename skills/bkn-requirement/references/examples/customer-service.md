# 案例：客户服务与销售运营 PRD 片段

## 业务需求

客服和销售团队希望 AI 汇总客户状态，识别流失风险，推荐下一步行动，并在遵守客户数据权限的前提下创建跟进任务。

## 场景总览

| 场景 | 用户 | 目标 | 优先级 |
|---|---|---|---|
| 查看客户健康状态 | 客户负责人 | 理解客户当前风险和变化原因 | P0 |
| 识别流失风险 | 销售经理 | 找出需要优先处理的客户 | P0 |
| 推荐下一步行动 | 客户负责人 | 获得可执行跟进建议 | P0 |
| 创建跟进任务 | 客户负责人 | 生成任务草案并分配责任人 | P1 |

## 场景需求详述

| 项目 | 内容 |
|---|---|
| 触发方式 | 客户健康分下降、服务工单激增、续约临近或用户主动查询。 |
| 当前流程 | 人工查看工单、商机、互动记录和客户负责人备注。 |
| 目标流程 | 系统汇总客户状态、风险驱动因素和建议行动，并生成跟进任务草案。 |
| 输入 | 客户、服务工单、商机、互动记录、续约日期、客户负责人。 |
| 输出 | 健康状态、流失风险、证据摘要、下一步建议、任务草案。 |
| 业务规则 | 敏感客户字段按角色控制；外发消息默认只生成草案；风险等级更新需要客户负责人审批。 |
| 异常边界 | 缺少近期互动或服务记录时，必须说明判断不充分。 |
| 交互期望 | 客户详情页展示风险解释、证据记录、建议行动和任务草案。 |

## 业务验收用例

| ID | 场景 | 用户输入 | 期望业务输出 | 通过标准 |
|---|---|---|---|---|
| AC-01 | 查看客户健康状态 | “为什么客户 A 被判断为高流失风险？” | 返回驱动因素和证据交互记录 | 证据可追溯 |
| AC-02 | 识别流失风险 | “本月哪些客户健康状态下降最快？” | 排名客户并展示变化原因 | 排序口径明确 |
| AC-03 | 推荐下一步行动 | “客户负责人下一步应该做什么？” | 推荐行动并说明原因 | 建议可执行 |
| AC-04 | 创建跟进任务 | “为客户 A 创建跟进任务。” | 生成任务草案、负责人和截止日期 | 不自动外发消息 |
| AC-05 | 权限边界 | “显示敏感联系人信息。” | 按角色权限控制可见性 | 未授权不可见 |

## BKN_Creator 交接线索

```yaml
bkn_creator_handoff:
  schema_version: bkn-requirement.v0.5
  business_confirmed:
    business_scenarios:
      - 查看客户健康状态
      - 识别流失风险
      - 推荐下一步行动
      - 创建跟进任务
    business_objects:
      - 客户
      - 联系人
      - 客户负责人
      - 服务工单
      - 销售商机
      - 客户互动
      - 跟进任务
    business_rules:
      - 敏感客户字段按角色控制访问。
      - 外发消息默认只生成草案。
      - 风险等级更新需要客户负责人审批。
  candidate_only:
    candidate_objects:
      - Customer
      - Contact
      - AccountOwner
      - ServiceTicket
      - SalesOpportunity
      - CustomerInteraction
      - ChurnRiskSignal
      - FollowUpTask
    candidate_relations:
      - Customer has Contact
      - Customer owned_by AccountOwner
      - ServiceTicket raised_by Customer
      - SalesOpportunity belongs_to Customer
    candidate_logic_properties:
      - Customer.customer_health_score
      - Customer.churn_risk_signal
    candidate_actions:
      - CreateFollowUpTask
      - UpdateCustomerRiskLevel
  needs_bkn_creator_decision:
    - ChurnRiskSignal 是否建为派生对象。
    - 客户健康分是指标型逻辑属性还是算子型逻辑属性。
    - 外发消息是否只能生成草案。
  critical_gaps:
    - 客户敏感字段权限矩阵未确认。
    - 健康分下降和流失风险标准答案样例未确认。
  requires_business_confirmation:
    - 风险等级更新审批人。
    - 任务草案默认负责人和截止日期规则。
```
