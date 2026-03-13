---
name: plurk-mcp-skills
description: plurk-mcp 的统一入口 skill。用于在 Load Profile、Load Alerts、Load Mentions、Create Post、Create Reply 这些具体技能之间做选择，并在进入具体技能前先提醒当前工具边界。
---

# plurk-mcp 统一入口

## 何时使用

- 用户只说“用 plurk-mcp 处理一下”，但还没有明确是读还是写
- 用户需要先在多个子技能之间选一个最合适的工作流
- 用户需要先快速了解当前 `plurk-mcp` 的能力边界，再进入具体操作

## 先读哪些参考

- 先读 `../_shared/plurk-mcp-contract.md`
- 再读 `../_shared/plurk-mcp-guardrails.md`
- 需要明确如何切换时，再读 `../_shared/plurk-mcp-workflows.md`

## 路由规则

- 查看当前认证账号资料
  切换到 `$plurk-mcp-load-profile`
- 查看近期 alerts
  切换到 `$plurk-mcp-load-alerts`
- 查看近期 mentions，或为回复准备上下文
  切换到 `$plurk-mcp-load-mentions`
- 创建新的 plurk
  切换到 `$plurk-mcp-create-post`
- 回复符合资格的互动
  切换到 `$plurk-mcp-create-reply`

## 工作方式

1. 先判断用户当前是“读取上下文”还是“执行写入”。
2. 不直接承担最终业务动作，而是把请求路由到最合适的子技能。
3. 在切换前，先提醒当前边界：只支持 `plurk_get_me`、`plurk_get_alerts`、`plurk_get_mentions_context`、`plurk_get_thread_context`、`plurk_post`、`plurk_reply`。
4. 如果用户请求超出边界，直接说明不支持，不要把它伪装成某个子技能可完成的任务。

## 不要做

- 不要把统一入口 skill 写成“大而全”的单体 skill。
- 不要在这里直接跳过上下文检查去执行发帖或回帖。
- 不要把 edit、delete、follow、fan-management 等动作路由成可用能力。
