# plurk-mcp 契约总览

## 定位

- `plurk-mcp` 是 OpenClaw 的执行层，不是内容策略层。
- 它支持 OpenClaw 在一次会话中操作多个 Plurk 账号；真正的目标账号由每次调用随请求提供的 `credentials` 决定。
- 服务端负责读取上下文、执行允许的动作，并按认证账号落实护栏；它不负责内容策略、排期或 campaign 决策。

## 调用前提

- 每次已支持工具调用都必须提供完整的 `credentials`：
  - `appKey`
  - `appSecret`
  - `accessToken`
  - `accessTokenSecret`
- 读取结果、写入结果、配额判断和 reply 冷却，都以这组 credentials 解析出的认证账号为准。
- 如果用户同时运营多个账号，但还不确定当前这组 credentials 会落到哪个账号，先用 `plurk_get_me` 确认。

## 当前支持的工具

- `plurk_get_me`
  读取 supplied credentials 对应认证账号的标准化 profile。
- `plurk_get_alerts`
  读取该账号近期标准化 alerts。
  可传 `limit`，范围 `1-100`，未指定时使用工具默认值。
- `plurk_get_mentions_context`
  读取该账号近期由 mention 驱动的交互上下文。
  可传 `limit`，范围 `1-100`，未指定时使用工具默认值。
- `plurk_get_thread_context`
  使用 supplied credentials 读取指定 `plurkId` 的父 plurk 与标准化 replies。
  `plurkId` 必须是正整数。
- `plurk_post`
  为 supplied credentials 对应的认证账号创建一条新的 plurk。
  `content` 必填；`qualifier` 可选，长度需在 `1-12` 个字符内。
- `plurk_reply`
  以 supplied credentials 对应的认证账号向符合资格的互动发送 reply。
  需要正整数 `plurkId`、非空 `content`，`qualifier` 可选且长度需在 `1-12` 个字符内。

## 当前明确不支持的动作

- edit plurk
- delete plurk
- follow user
- fan-management actions
- 参与无关的公共线程
