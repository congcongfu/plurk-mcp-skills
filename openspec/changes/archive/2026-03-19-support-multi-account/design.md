## Context

`plurk-mcp` 现在已经是 request-scoped credentials 模型：MCP tool schema 要求每次调用携带 `credentials`，服务端会用该 credentials bundle 解析认证账号，并把发帖配额、reply 冷却和审计归属按账号隔离。当前 skill pack 仍保留了明显的单账号表述，例如“当前绑定的是哪个账号”“当前认证账号”，这会让 OpenClaw 在多账号运营时误以为服务端启动后只绑定一个账号。

这次 change 的工作重点是同步 skill pack 的操作语义，而不是改上游执行层。约束也比较明确：

- 不能把未支持动作写成新能力。
- 不能让 skill pack 自己承担 credentials 存储、命名账号管理或 OAuth 发放流程。
- 需要兼容现有的六个技能结构，不重做 skill pack 目录。
- 需要尽量少碰已经有定制内容的 `plurk-mcp-create-post`，避免和既有内容策略改动相互覆盖。

## Goals / Non-Goals

**Goals:**
- 让共享参考资料明确反映“每次工具调用都要带 credentials”的契约。
- 让统一入口和各子技能都把“锁定目标账号/credentials bundle”作为多账号场景下的显式前置动作。
- 让技能侧对配额、冷却和资格边界的描述切换到“按认证账号隔离”的模型。
- 在发帖与回帖工作流中补上“写入将落到哪个账号”的确认语义，减少多账号误发。
- 同步更新 OpenClaw agent 元数据，使入口提示不再暗示只有一个当前账号。

**Non-Goals:**
- 不修改上游 `plurk-mcp` 的 MCP tool surface、debug console 或服务端策略实现。
- 不在 skill pack 中引入账号别名注册表、本地 secret 缓存或 OAuth 登录页面。
- 不改变 Laike 内容策略本身，只在必要位置补充账号选择与写入归属说明。
- 不追求完全自动推断用户想用哪一个账号；如果目标账号不清楚，skill 仍应先澄清或先看 profile。

## Decisions

### 用“目标账号 = 本次 credentials 所解析出的认证账号”作为统一术语

共享参考、统一入口和具体 skill 都统一改用“这组 credentials 对应的认证账号”“本次调用的目标账号”这类说法，避免继续使用“当前绑定账号”“服务当前使用的账号”这类启动期单例语义。

这样做的好处是：

- 和 `plurk-mcp` 当前 tool schema 保持一致。
- 能自然覆盖 OpenClaw 在一个会话里切换多个账号的场景。
- 让“先用 `plurk_get_me` 确认账号，再继续读写”成为一条明确工作流。

备选方案：

- 继续使用“当前认证账号”但不解释来源：太含糊，仍容易让人理解为进程级单账号。
- 只用用户口头指定的昵称代表账号：昵称不是执行层真实凭证，不能替代 credentials bundle。

### 把多账号前置动作沉到共享参考和每个子技能的首步，而不是单独新增一个账号管理技能

这次不会新增第七个“账号切换”技能。相反，统一入口和各个读写技能都会补一条轻量前置规则：当请求涉及多个账号，或用户没有锁定目标 credentials 时，先澄清要操作哪一组 credentials；必要时先切到 `plurk-mcp-load-profile` 用 `plurk_get_me` 确认。

这样能复用现有技能集合，同时保持：

- 入口 skill 仍只做路由，不承担完整执行。
- `Load Profile` 继续是只读能力，但多了“为后续写入确认账号”的职责。
- 其它 skill 不必重复解释整套 credentials schema，只需强调“使用将要操作的那组 credentials”。

备选方案：

- 只改共享参考，不改子技能：用户容易跳过共享参考，具体 skill 仍会沿用旧心智模型。
- 新增独立账号切换技能：会让技能切分变复杂，而且底层并没有独立的“切换账号”动作，只有更换 request credentials。

### 写入技能在锁定内容与线程目标之外，还要锁定写入账号

`plurk_post` 和 `plurk_reply` 都已经由服务端按账号做策略检查，但到了服务端才发现“用错账号”太晚了。技能层在真正写入前，应该把“这次要用哪个账号发/回”也作为显式确认的一部分。

具体做法：

- `Create Post` 在进入最终发布前，要求复述要使用的目标账号或对应 credentials。
- `Create Reply` 在复述 `plurkId`、回复对象和资格依据时，同时复述回复将从哪个认证账号发出。
- 如果用户同时提到多个账号，但没有说明当前要用哪一个，skill 不直接进入写入。

备选方案：

- 仅依赖服务端审计与配额结果发现账号错误：反馈时机太晚，且无法避免误发。
- 仅在 `Load Profile` 里处理账号确认：用户可能直接从入口进入写入 skill，仍会漏掉确认。

### 元数据提示词同步收敛到“指定账号”的表达

OpenClaw UI 入口会直接展示 `agents/openai.yaml` 里的描述与默认提示。如果这些元数据继续写“当前认证账号”“直接进入发帖/回帖”，用户会在进入 skill 前就收到错误暗示。因此至少入口、Profile，以及发帖/回帖相关的 agent 元数据也要同步改成“指定账号/目标账号”的表达。

备选方案：

- 只改 `SKILL.md`：对已经依赖 metadata 的入口体验覆盖不够完整。

## Risks / Trade-offs

- [多账号前置确认会增加一步交互] -> 只在目标账号不明确时触发，并优先复用 `Load Profile` 作为轻量确认步骤。
- [具体 skill 对 credentials 说明过多会显得啰嗦] -> 把完整契约留在共享参考，子技能只保留“先锁定目标账号/credentials”的最小提示。
- [`plurk-mcp-create-post` 已有较多定制内容] -> 只做局部增量修改，避免重写现有内容策略段落。
- [skills 与上游实现再次漂移] -> 直接基于 `README`、`toolCatalog.ts`、`plurkApplication.ts` 和 `appConfig.ts` 里的已实现行为同步措辞。

## Migration Plan

1. 在共享参考中替换单账号表述，补充 request-scoped credentials 与按账号隔离的护栏说明。
2. 更新统一入口与六个子技能的说明文字，把“锁定目标账号/credentials”加到合适的工作流节点。
3. 更新受影响的 `agents/openai.yaml`，使 UI 默认提示词不再暗示单账号模型。
4. 用全文搜索确认仓库中不再把 `plurk-mcp` 说成“面向单一账号工作”或“服务当前绑定某账号”。

## Open Questions

None.
