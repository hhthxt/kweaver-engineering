# 案例：运营告警分诊 PRD 片段

## 业务需求

运营分析师需要查看告警收件箱，对负责路线上的告警进行分诊，并根据优先级、路线详情、航班详情和组织影响，重新分派、解决或升级告警。

## 场景总览

| 场景 | 用户 | 目标 | 优先级 |
|---|---|---|---|
| 查看负责路线告警 | 运营分析师 | 找到需要优先处理的告警 | P0 |
| 告警分诊 | 运营分析师 | 判断重分派、解决或升级 | P0 |
| 跨团队升级 | 运营分析师、负责人 | 对高影响告警升级处理 | P1 |

## 场景需求详述

| 项目 | 内容 |
|---|---|
| 触发方式 | 分析师打开告警收件箱或收到高优先级告警通知。 |
| 当前流程 | 人工查看路线、航班、影响范围和负责人，再判断处理方式。 |
| 目标流程 | 系统按优先级和组织影响排序告警，展示证据，并生成处理建议。 |
| 输入 | 告警、路线、航班、负责人、影响范围、当前处理状态。 |
| 输出 | 告警优先级、影响解释、推荐处理动作、所需审批或原因。 |
| 业务规则 | 升级必须填写原因；解决必须填写处理说明；跨团队分派需要负责人权限。 |
| 异常边界 | 缺少航班影响或路线负责人时，不输出确定性升级建议。 |
| 交互期望 | 收件箱支持筛选、排序、详情钻取、备注、转派、解决和升级草案。 |

## 业务验收用例

| ID | 场景 | 用户输入 | 期望业务输出 | 通过标准 |
|---|---|---|---|---|
| AC-01 | 查看负责路线告警 | “哪些高优先级告警影响我负责的路线？” | 返回按优先级排序的告警和证据 | 路线归属和优先级正确 |
| AC-02 | 告警分诊 | “为什么这个告警应该升级？” | 返回影响范围、航班、路线和升级原因 | 证据完整 |
| AC-03 | 跨团队升级 | “升级告警 A-123。” | 生成升级草案，并要求填写原因 | 不直接无理由升级 |
| AC-04 | 权限边界 | “解决其他团队负责的告警。” | 拒绝或请求授权后转派 | 权限边界正确 |

## BKN_Creator 交接线索

```yaml
bkn_creator_handoff:
  schema_version: bkn-requirement.v0.5
  business_confirmed:
    business_scenarios:
      - 查看负责路线告警
      - 告警分诊
      - 跨团队升级
    business_objects:
      - 告警
      - 路线
      - 航班
      - 团队
      - 处理人
    business_rules:
      - 升级必须填写原因。
      - 解决必须填写处理说明。
      - 跨团队分派需要负责人权限。
  candidate_only:
    candidate_objects:
      - AlertTicket
      - Route
      - Flight
      - Team
      - Employee
    candidate_relations:
      - Employee responsible_for Route
      - AlertTicket affects Route
      - AlertTicket assigned_to Employee
    candidate_logic_properties:
      - AlertTicket.alert_priority_score
    candidate_actions:
      - ReassignAlert
      - ResolveAlert
      - EscalateAlert
  needs_bkn_creator_decision:
    - Route 是否建为派生对象，还是作为 Flight 的组合属性。
    - 优先级判断是指标型逻辑属性还是算子型逻辑属性。
    - 升级和跨团队分派是否只能生成草案。
  critical_gaps:
    - 路线负责人数据源和权限边界未确认。
    - 告警优先级规则和标准答案样例未确认。
  requires_business_confirmation:
    - 高优先级告警定义。
    - 跨团队分派审批责任人。
```
