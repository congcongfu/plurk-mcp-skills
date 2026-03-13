---
name: plurk-mcp-load-mentions
description: 在用户要求查看近期 mentions、梳理可回复互动，或为后续回复准备上下文时使用。通过 plurk_get_mentions_context 读取 mention 结果，并按需使用 plurk_get_thread_context 展开线程，但整体保持只读。
---

# 加载 Plurk Mentions

## 何时使用

- 用户要查看近期 mentions
- 用户要整理哪些互动值得后续回复
- 用户需要先读上下文，再决定是否切换到回帖工作流

## 先读哪些参考

- 先读 `../_shared/plurk-mcp-contract.md`
- 再读 `../_shared/plurk-mcp-workflows.md`
- 需要确认资格边界时，再读 `../_shared/plurk-mcp-guardrails.md`

## 工作流

1. 调用 `plurk_get_mentions_context` 获取近期由 mention 驱动的交互。
2. 如果某一条 mention 需要更深的线程信息，再调用 `plurk_get_thread_context` 展开指定 `plurkId`。
3. 继续保持只读，总结 mention 的上下文、可能的回复对象和需要注意的 thread。
4. 如果用户决定真的要回复，明确切换到 `$plurk-mcp-create-reply`。

## 不要做

- 不要因为看到了 mention 就直接调用 `plurk_reply`。
- 不要在没有 `plurkId` 和 thread context 的情况下猜测 thread 走向。
- 不要把 mention 读取结果描述成已经通过资格校验。
