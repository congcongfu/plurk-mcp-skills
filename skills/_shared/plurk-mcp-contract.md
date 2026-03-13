# plurk-mcp 契约总览

## 定位

- `plurk-mcp` 是 OpenClaw 的执行层，不是内容策略层。
- 它面向单一 Plurk 账号工作，负责读取上下文、执行允许的动作，并在服务端落实护栏。

## 当前支持的工具

- `plurk_get_me`
  读取当前认证账号的标准化 profile。
- `plurk_get_alerts`
  读取近期标准化 alerts。
  可传 `limit`，范围 `1-100`，未指定时使用工具默认值。
- `plurk_get_mentions_context`
  读取近期由 mention 驱动的交互上下文。
  可传 `limit`，范围 `1-100`，未指定时使用工具默认值。
- `plurk_get_thread_context`
  读取指定 `plurkId` 的父 plurk 与标准化 replies。
  `plurkId` 必须是正整数。
- `plurk_post`
  创建一条新的 plurk。
  `content` 必填；`qualifier` 可选，长度需在 `1-12` 个字符内。
- `plurk_reply`
  向符合资格的互动发送 reply。
  需要正整数 `plurkId`、非空 `content`，`qualifier` 可选且长度需在 `1-12` 个字符内。

## 当前明确不支持的动作

- edit plurk
- delete plurk
- follow user
- fan-management actions
- 参与无关的公共线程
