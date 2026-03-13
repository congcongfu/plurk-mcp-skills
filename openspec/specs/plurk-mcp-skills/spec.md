# plurk-mcp-skills Specification

## Purpose
TBD - created by archiving change init-skills. Update Purpose after archive.
## Requirements
### Requirement: 技能包需要文档化当前 plurk-mcp 契约
技能包 SHALL 提供共享参考资料，准确反映上游 `plurk-mcp` 当前的工具面、支持的写操作边界，以及已经由服务端强制执行的护栏。

#### Scenario: 共享参考资料只列出已批准工具
- **WHEN** 操作员或 agent 阅读本仓库中的共享 `plurk-mcp` 参考资料
- **THEN** 文档中只描述 `plurk_get_me`、`plurk_get_alerts`、`plurk_get_mentions_context`、`plurk_get_thread_context`、`plurk_post` 和 `plurk_reply`，且不会把未支持动作写成可用工具

#### Scenario: 共享参考资料覆盖已生效的安全规则
- **WHEN** 操作员或 agent 阅读写操作相关的共享护栏说明
- **THEN** 文档会明确说明新 plurk 受每日配额限制、reply 不占用每日新帖配额、reply 只能发生在符合资格的交互上，且同线程 reply 还受 MCP 服务端冷却策略约束

### Requirement: 技能包需要交付首版 OpenClaw 技能集合
技能包 SHALL 交付六个可安装技能：`plurk-mcp-skills`、`plurk-mcp-load-profile`、`plurk-mcp-load-alerts`、`plurk-mcp-load-mentions`、`plurk-mcp-create-post` 和 `plurk-mcp-create-reply`，并且每个技能 SHALL 同时包含必需的 `SKILL.md` 元数据与面向 OpenClaw 的 agent 元数据。

#### Scenario: 检查已安装的技能目录
- **WHEN** 操作员检查本仓库中打包后的技能目录
- **THEN** 仓库中会存在 `plurk-mcp-skills`、`plurk-mcp-load-profile`、`plurk-mcp-load-alerts`、`plurk-mcp-load-mentions`、`plurk-mcp-create-post` 和 `plurk-mcp-create-reply` 六个目录，并且每个目录都包含 `SKILL.md` 与 `agents/openai.yaml`

### Requirement: 技能包需要采用可开源发布的公共目录结构
技能包 SHALL 将对外发布的技能放在仓库级 `skills/` 目录下，并将共享参考资料放在 `skills/_shared/` 中，使该仓库既能作为本地路径 skill pack 被 OpenClaw 加载，也适合公开发布。

#### Scenario: 通过仓库根目录加载 skill pack
- **WHEN** 操作员把本仓库根目录作为 OpenClaw 的 `skills.load.extraDirs` 配置项
- **THEN** OpenClaw 可以从嵌套的 `skills/` 目录发现统一入口 skill 和五个具体技能，而不要求操作员手动指向内部开发目录

### Requirement: 技能包需要提供跨平台可发现的统一入口 skill
技能包 SHALL 提供一个名为 `plurk-mcp-skills` 的统一入口 skill，用于在进入具体读写工作流之前，把请求路由到合适的子技能，并提醒当前支持边界。

#### Scenario: 从统一入口切换到具体子技能
- **WHEN** 用户的请求只表达了“使用 plurk-mcp”，但还没有明确是哪一类工作流
- **THEN** `plurk-mcp-skills` 会先根据请求类型在读取类和写入类子技能之间做路由，而不是直接承担所有具体动作

### Requirement: Load Profile 技能必须保持只读且聚焦账号资料
`plurk-mcp-load-profile` 技能 SHALL 指导 agent 使用 `plurk_get_me` 获取认证账号资料，且 SHALL 不在该技能内部引导任何写操作。

#### Scenario: 加载操作员账号资料
- **WHEN** 用户要求 agent 加载或检查当前配置的 Plurk 账号资料
- **THEN** skill 会指导 agent 使用 `plurk_get_me` 并返回标准化后的 profile 信息，而不会调用任何写工具

### Requirement: Load Alerts 技能必须保持只读且聚焦提醒信息
`plurk-mcp-load-alerts` 技能 SHALL 指导 agent 使用 `plurk_get_alerts` 获取近期 alerts，且 SHALL 不在该技能内部引导任何写操作。

#### Scenario: 加载近期提醒
- **WHEN** 用户要求 agent 查看来自 `plurk-mcp` 的近期 alerts
- **THEN** skill 会指导 agent 使用 `plurk_get_alerts` 并总结返回的标准化 alert 数据，而不会调用任何写工具

### Requirement: Load Mentions 技能需要读取 mentions 上下文并支持可选线程展开
`plurk-mcp-load-mentions` 技能 SHALL 指导 agent 使用 `plurk_get_mentions_context` 获取近期由 mention 驱动的交互，并且 MAY 在需要补充回帖上下文时使用 `plurk_get_thread_context`，但整体流程仍保持只读。

#### Scenario: 加载近期 mention 上下文
- **WHEN** 用户要求 agent 加载或总结近期 mentions
- **THEN** skill 会指导 agent 使用 `plurk_get_mentions_context`，并在需要更清晰线程信息时补充调用 `plurk_get_thread_context`，且不会调用任何写工具

### Requirement: Create Post 技能必须使用受护栏保护的新帖工作流
`plurk-mcp-create-post` 技能 SHALL 指导 agent 起草新 plurk、确认最终要发布的内容，并将 `plurk_post` 作为创建新帖的唯一写步骤。

#### Scenario: 发布新的 plurk
- **WHEN** 用户要求 agent 通过 `plurk-mcp` 发布新的 plurk
- **THEN** skill 会指导 agent 先整理待发布内容，并在最终写入时使用 `plurk_post`

#### Scenario: 每日配额阻止新帖发布
- **WHEN** `plurk_post` 因服务端每日新帖配额耗尽而被拒绝
- **THEN** skill 会把这次拒绝当作策略边界进行反馈，而不会建议任何不被支持的绕过行为

### Requirement: Create Reply 技能必须在写入前检查上下文和回帖边界
`plurk-mcp-create-reply` 技能 SHALL 要求 agent 在回帖前先检查 thread context，并且 SHALL 只把“显式 mention 操作员”或“回复发生在操作员自己发布的 plurk 线程中”视为有效回帖场景。

#### Scenario: 回应符合资格的交互
- **WHEN** 用户要求 agent 回复一个显式 mention，或回复一个属于操作员自有线程的互动
- **THEN** skill 会先指导 agent 检查 thread context，然后再使用 `plurk_reply` 完成最终写操作

#### Scenario: 请求超出回帖策略范围
- **WHEN** 用户要求 agent 回复一个既不属于操作员自有线程、也没有显式 mention 操作员的讨论
- **THEN** skill 不会引导 agent 绕过策略，而是明确提示该回复请求超出了当前支持的 MCP 工作流范围

