---
name: plurk-mcp-create-post
description: 在用户已经明确要发布新 plurk，或需要先整理内容再执行发布时使用。通过 plurk_post 执行最终写操作，并遵守每日新帖配额和当前不支持动作的边界。
---

# 创建 Plurk Post

## 何时使用

- 用户明确要求发布一条新的 plurk
- 用户已经有草稿，需要你帮助整理后再发布
- 用户想确认发布内容和 qualifier 后执行一次受护栏保护的写入

## 先读哪些参考

- 先读 `../_shared/plurk-mcp-contract.md`
- 再读 `../_shared/plurk-mcp-guardrails.md`
- 需要跨技能切换时，再读 `../_shared/plurk-mcp-workflows.md`

## 工作流

1. 先确认最终要发布的 `content`。如果用户还在讨论文案，只帮他整理，不要提前发布。
2. 如果文案经过你整理、改写、翻译或补全，先展示最终版本，并拿到一次明确的“确认发布”再继续。
3. 如需 `qualifier`，确认其存在且长度保持在 1 到 12 个字符内。
4. 只有在用户已经明确要求现在发布，且最终内容已经锁定时，才调用 `plurk_post`。
5. 返回写入结果，并明确说明这是一次新帖写操作。
6. 如果命中每日配额或其他策略拒绝，直接把它当作服务端边界反馈出来，不要建议绕过。

## 不要做

- 不要承诺 edit、delete、schedule、follow 或 fan-management 之类当前不支持的动作。
- 不要在一次请求里反复重试 `plurk_post`。
- 不要把 brainstorming 状态误当成“用户已确认发布”。
- 不要把“帮我润色一下”或“给我起个草稿”直接升级成实际发帖。
