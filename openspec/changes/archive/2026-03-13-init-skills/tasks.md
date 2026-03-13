## 1. 共享基础

- [x] 1.1 为首版 `plurk-mcp` 技能包创建面向开源分发的 `skills/` 目录结构
- [x] 1.2 添加共享参考文件，概述当前 `plurk-mcp` 的工具清单、写操作边界和服务端护栏，并明确 reply 不占用每日新帖配额
- [x] 1.3 整理共享表述、仓库入口文件和参考结构，让多个技能可以引用同一份上游契约而不重复复制
- [x] 1.4 创建跨平台可发现的统一入口 skill，并让其路由到五个具体子技能

## 2. Load Profile 技能

- [x] 2.1 创建 `plurk-mcp-load-profile/SKILL.md`，用于通过 `plurk_get_me` 只读加载认证后的账号资料
- [x] 2.2 添加 `plurk-mcp-load-profile/agents/openai.yaml`，并使元数据与该工作流对齐

## 3. Load Alerts 技能

- [x] 3.1 创建 `plurk-mcp-load-alerts/SKILL.md`，用于通过 `plurk_get_alerts` 只读加载提醒信息
- [x] 3.2 添加 `plurk-mcp-load-alerts/agents/openai.yaml`，并接入共享参考资料

## 4. Load Mentions 技能

- [x] 4.1 创建 `plurk-mcp-load-mentions/SKILL.md`，用于通过 `plurk_get_mentions_context` 只读加载 mentions 上下文
- [x] 4.2 增加 `plurk_get_thread_context` 的可选使用说明，用于在需要更深线程上下文时补充信息
- [x] 4.3 添加 `plurk-mcp-load-mentions/agents/openai.yaml`，并接入共享参考资料

## 5. Create Post 技能

- [x] 5.1 创建 `plurk-mcp-create-post/SKILL.md`，用于通过 `plurk_post` 起草并发布新 plurk
- [x] 5.2 在发帖工作流中写明每日配额和不支持动作的边界，不承诺任何绕过策略的行为
- [x] 5.3 添加 `plurk-mcp-create-post/agents/openai.yaml`，并接入共享参考资料

## 6. Create Reply 技能

- [x] 6.1 创建 `plurk-mcp-create-reply/SKILL.md`，用于在调用 `plurk_reply` 前先检查 thread context 的回帖工作流
- [x] 6.2 编码“自有线程”和“显式 mention”两类回帖资格边界，并补充带冷却意识的回帖说明
- [x] 6.3 添加 `plurk-mcp-create-reply/agents/openai.yaml`，并接入共享参考资料

## 7. 校验与验证

- [x] 7.1 检查每个 skill 的 `name` 与 `description` 元数据是否准确，内部引用路径是否有效
- [x] 7.2 以仓库根目录作为本地路径在 OpenClaw/Codex 中做一次 smoke test，确认这些技能可以被发现，且生成的元数据与预期工作流一致
- [x] 7.3 将最终 skill 内容与当前 `plurk-mcp` 的 README 和 spec 对照，避免在实现完成前出现超出支持范围或内容漂移
