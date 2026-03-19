# plurk-mcp 技能切换图

所有工作流都针对“本次 supplied credentials 对应的认证账号”执行；如果当前请求涉及多个账号但还没锁定目标账号，先走 `plurk-mcp-load-profile`。

## 只读技能

- `plurk-mcp-load-profile`
  只读查看某组 credentials 对应的账号资料，并确认后续动作会落到哪个账号。
- `plurk-mcp-load-alerts`
  只读查看目标账号的近期 alerts。
- `plurk-mcp-load-mentions`
  只读查看目标账号的近期 mentions，并按需展开 thread context。

## 写入技能

- `plurk-mcp-create-post`
  先确认目标账号和最终内容，再调用 `plurk_post`。
- `plurk-mcp-create-reply`
  先确认目标账号、读取 thread context、确认资格边界，再调用 `plurk_reply`。

## 何时切换

- 如果用户还没锁定当前要操作的账号或 credentials，先切换到 `$plurk-mcp-load-profile`。
- 如果用户只是看数据，不要从只读技能直接跳成写入。
- 如果用户在看 mentions 后决定回帖，切换到 `$plurk-mcp-create-reply`。
- 如果用户在看资料或提醒后决定发帖，切换到 `$plurk-mcp-create-post`。
- 切换时要显式说明已经从读取工作流进入写入工作流。
