---
name: plurk-mcp-create-reply
description: 在用户要求回复明确 mention 或操作员自有线程中的互动时使用。先读取 thread context，再通过 plurk_reply 执行最终写入，并遵守资格与冷却边界。
---

# 创建 Plurk Reply

## 何时使用

- 用户明确要求回复某条 mention
- 用户要回复操作员自己发布的 plurk 线程中的互动
- 用户已经决定回帖，需要你先检查上下文和资格边界

## 先读哪些参考

- 先读 `../_shared/plurk-mcp-contract.md`
- 再读 `../_shared/plurk-mcp-guardrails.md`
- 需要从读取工作流切换过来时，再读 `../_shared/plurk-mcp-workflows.md`

## 工作流

1. 先确认目标 `plurkId`。如果请求来自“最近 mentions”，但目标 thread 还不够清楚，可以先配合使用 `plurk_get_mentions_context`。
2. 在回帖前调用 `plurk_get_thread_context`，不要跳过这一步。
3. 只有当目标属于“显式 mention 操作员”或“操作员自有线程”时，才继续准备回复内容。
4. 确认最终 `content`。如需 `qualifier`，确认其长度保持在 1 到 12 个字符内。
5. 调用 `plurk_reply` 执行最终写入。
6. 如果命中资格拒绝或同线程冷却，直接说明是服务端边界，不要建议绕过。

## 不要做

- 不要回复无关公共线程。
- 不要在没有读取 thread context 的情况下直接写入。
- 不要把资格是否通过完全交给猜测；如果边界不清楚，就停下来说明原因。
