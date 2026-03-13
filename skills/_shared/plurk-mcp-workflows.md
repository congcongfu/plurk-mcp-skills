# plurk-mcp 技能切换图

## 只读技能

- `plurk-mcp-load-profile`
  只读查看当前认证账号资料。
- `plurk-mcp-load-alerts`
  只读查看近期 alerts。
- `plurk-mcp-load-mentions`
  只读查看近期 mentions，并按需展开 thread context。

## 写入技能

- `plurk-mcp-create-post`
  先确认最终内容，再调用 `plurk_post`。
- `plurk-mcp-create-reply`
  先读取 thread context、确认资格边界，再调用 `plurk_reply`。

## 何时切换

- 如果用户只是看数据，不要从只读技能直接跳成写入。
- 如果用户在看 mentions 后决定回帖，切换到 `$plurk-mcp-create-reply`。
- 如果用户在看资料或提醒后决定发帖，切换到 `$plurk-mcp-create-post`。
- 切换时要显式说明已经从读取工作流进入写入工作流。
