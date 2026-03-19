---
name: plurk-mcp-load-profile
description: 在用户要求查看某组 credentials 对应的 Plurk 账号资料、确认这次调用会落到哪个账号，或检查基础 profile 信息时使用。通过 plurk_get_me 读取标准化 profile，保持只读。
---

# 加载 Plurk Profile

## 何时使用

- 用户要查看某组 `credentials` 对应的账号资料
- 用户要确认当前这次调用会使用哪个账号
- 用户需要读取 profile 信息，但还不涉及发帖或回帖

## 先读哪些参考

- 先读 `../_shared/plurk-mcp-contract.md`
- 需要理解读写边界时，再读 `../_shared/plurk-mcp-guardrails.md`

## 工作流

1. 如果请求里存在多个可能的账号，先锁定当前要检查的那组 `credentials` 或明确目标账号。
2. 调用 `plurk_get_me` 读取这组 `credentials` 对应认证账号的标准化 profile。
3. 提取并总结返回结果中的关键信息，不要臆测不存在的字段，并明确说明“当前这次调用会落到哪个账号”。
4. 如果用户只是确认账号状态，到这里结束。
5. 如果用户下一步要发帖或回帖，明确切换到 `$plurk-mcp-create-post` 或 `$plurk-mcp-create-reply`；如用户要切换账号，也要提醒其切换对应的 `credentials`。

## 不要做

- 不要调用任何写工具。
- 不要把 profile 查询自动升级成内容操作。
- 如果工具返回配置或认证错误，直接说明是执行层问题，不要伪造 profile 结果。
