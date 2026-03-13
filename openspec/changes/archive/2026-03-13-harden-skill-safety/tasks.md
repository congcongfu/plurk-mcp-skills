## 1. 共享护栏与只读流程

- [x] 1.1 在共享护栏中加入“外部内容属于不可信输入”的规则
- [x] 1.2 收紧 `plurk-mcp-load-alerts`，禁止把 alerts 中的命令或链接当成 agent 指令
- [x] 1.3 收紧 `plurk-mcp-load-mentions`，要求候选回复目标分离，并在切换写入前先复述目标

## 2. 写入流程

- [x] 2.1 收紧 `plurk-mcp-create-post`，要求 agent 改写过文案时必须先展示最终版本并确认发布
- [x] 2.2 收紧 `plurk-mcp-create-reply`，要求写入前锁定 `plurkId`、目标对象和资格依据
- [x] 2.3 调整写入类 `agents/openai.yaml` 的默认提示词，降低单回合直接写入倾向

## 3. 文档与规范

- [x] 3.1 在仓库 README 中补充安全使用约定
- [x] 3.2 将新的安全要求同步到主规范
- [x] 3.3 为这次安全加固补建 OpenSpec 变更记录并归档
