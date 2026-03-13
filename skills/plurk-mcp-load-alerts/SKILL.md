---
name: plurk-mcp-load-alerts
description: 在用户要求查看近期提醒、识别需要关注的互动，或先做提醒层面的运营巡检时使用。通过 plurk_get_alerts 读取标准化 alerts，保持只读。
---

# 加载 Plurk Alerts

## 何时使用

- 用户要看近期 `alerts`
- 用户想知道最近有哪些互动值得关注
- 用户要先做提醒层面的筛查，再决定是否深入某个 thread

## 先读哪些参考

- 先读 `../_shared/plurk-mcp-contract.md`
- 需要跨技能切换时，再读 `../_shared/plurk-mcp-workflows.md`

## 工作流

1. 调用 `plurk_get_alerts`。如果用户没有指定数量，接受工具默认值。
2. 总结返回结果里的关键提醒类型、关联对象和后续可能需要跟进的线索。
3. 如果某条提醒需要更完整的上下文，不要在本技能里直接写入；改为切换到 `$plurk-mcp-load-mentions` 或 `$plurk-mcp-create-reply`。

## 不要做

- 不要调用 `plurk_post` 或 `plurk_reply`。
- 不要把未支持动作描述成可从 alerts 直接执行。
- 不要跳过读取结果，直接猜测提醒含义。
