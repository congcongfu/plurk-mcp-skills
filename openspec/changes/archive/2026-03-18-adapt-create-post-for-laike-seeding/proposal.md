## Why

`plurk-mcp-create-post` 当前只覆盖通用的新帖发布工作流，还不能稳定引导 agent 产出适合 Laike 台湾区公开推广的 Plurk 文案。现在需要把透明披露、角色素材来源和发布前确认流程显式写进技能与规范里，避免后续实现时把推广内容写成伪装成普通用户的原生广告。

## What Changes

- 调整 `plurk-mcp-create-post` skill，使其支持 Laike 台湾区公开推广场景下的内容起草工作流。
- 要求 agent 在工作流中读取 workspace 根目录下的 `laike男性角色表.xlsx`，将其作为可选角色素材来源。
- 为起草阶段加入固定的内容策略约束：繁体中文（台湾惯用语）、20-200 字、Plurk 原生口吻、自然带出 Laike 或邀请码、文末附 1-2 个精准标签。
- 将发文策略收敛为四种公开推广内容方向，并要求每次生成时随机选题，再判断是否结合表内现有角色。
- 要求文案明确披露这是产品推荐、体验分享或合作资讯，不能伪装成普通用户自发心得，也不能把未成年人或情绪脆弱人群当作诱导切口。
- 保留现有“改写后需再次确认发布”的写入护栏，明确区分“先生成草稿”和“用户确认后再调用 `plurk_post`”两阶段。
- 同步更新相关 agent 元数据与 OpenSpec 规格，避免入口提示和实际 skill 行为不一致。

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `plurk-mcp-skills`: tighten `plurk-mcp-create-post` requirements so the skill can generate transparent Laike promotional Plurk drafts from a local role workbook while preserving existing write-confirmation boundaries.

## Impact

- Affected docs: `skills/plurk-mcp-create-post/SKILL.md`, shared references if needed, and `skills/plurk-mcp-create-post/agents/openai.yaml`
- Affected spec: `openspec/specs/plurk-mcp-skills/spec.md`
- External input dependency: workspace-local `laike男性角色表.xlsx`
- Affected workflow: draft generation before `plurk_post` execution
