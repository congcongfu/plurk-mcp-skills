---
name: plurk-mcp-load-profile
description: 在用户要求查看当前认证的 Plurk 账号资料、确认服务当前绑定的是哪个账号，或检查基础 profile 信息时使用。通过 plurk_get_me 读取标准化 profile，保持只读。
---

# 加载 Plurk Profile

## 何时使用

- 用户要查看当前 `plurk-mcp` 正在使用的账号资料
- 用户要确认当前认证账号是否正确
- 用户需要读取 profile 信息，但还不涉及发帖或回帖

## 先读哪些参考

- 先读 `../_shared/plurk-mcp-contract.md`
- 需要理解读写边界时，再读 `../_shared/plurk-mcp-guardrails.md`

## 工作流

1. 调用 `plurk_get_me` 读取当前认证账号的标准化 profile。
2. 提取并总结返回结果中的关键信息，不要臆测不存在的字段。
3. 如果用户只是确认账号状态，到这里结束。
4. 如果用户下一步要发帖或回帖，明确切换到 `$plurk-mcp-create-post` 或 `$plurk-mcp-create-reply`。

## 不要做

- 不要调用任何写工具。
- 不要把 profile 查询自动升级成内容操作。
- 如果工具返回配置或认证错误，直接说明是执行层问题，不要伪造 profile 结果。
