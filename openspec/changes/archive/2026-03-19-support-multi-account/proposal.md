## Why

`plurk-mcp` 已经从“进程启动时绑定单一账号”的模型切换成“每次调用随请求提供 credentials、按账号隔离策略状态”的模型，但当前 skill pack 仍把它描述成单账号执行层，并在多个子技能里默认存在一个“当前绑定账号”。如果不补这轮变更，OpenClaw 在运营多个 Plurk 账号时就容易把账号选择、配额理解和回帖边界讲错。

## What Changes

- 更新共享契约文档，明确所有已支持工具都要求在每次调用时提供完整的 Plurk credentials，并且每次调用都针对该 credentials 所解析出的认证账号执行。
- 更新统一入口和各个读写子技能，要求 agent 在用户意图涉及多个账号时先锁定目标账号或 credentials bundle，而不是假定服务端已经预先绑定某个账号。
- 更新共享护栏说明，明确每日发帖配额、同线程 reply 冷却和审计归属都按认证账号隔离，而不是由所有账号共用一个全局桶。
- 调整 `Load Profile` 的职责描述，使其既能查看某组 credentials 对应的账号资料，也能在写入前帮助确认“当前这次调用会落到哪个账号”。
- 同步更新 OpenClaw agent 元数据和提示文案，避免入口提示、共享参考和具体 skill 行为继续沿用单账号表述。

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `plurk-mcp-skills`: revise the skill pack contract and workflow guidance from a startup-bound single-account model to request-scoped multi-account operation.

## Impact

- Affected docs: `skills/_shared/plurk-mcp-contract.md`, `skills/_shared/plurk-mcp-guardrails.md`, `skills/_shared/plurk-mcp-workflows.md`
- Affected skills: `skills/plurk-mcp-skills`, `skills/plurk-mcp-load-profile`, `skills/plurk-mcp-load-alerts`, `skills/plurk-mcp-load-mentions`, `skills/plurk-mcp-create-post`, `skills/plurk-mcp-create-reply`
- Affected metadata: `agents/openai.yaml` prompts that currently imply a single “current account”
- Upstream references used for alignment: `plurk-mcp` README plus request-scoped credential handling in `src/transports/mcp/toolCatalog.ts`, `src/services/plurkApplication.ts`, and `src/config/appConfig.ts`
