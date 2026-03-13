---
name: plurk-mcp-skill-pack
description: plurk-mcp skill pack 的仓库级说明文件。用于解释本仓库的结构、共享参考和统一入口 skill 的位置，而不是作为实际安装后的子 skill 使用。
---

# plurk-mcp Skill Pack 说明

## 用途

这是仓库级说明文件，用于描述这个 skill pack 的结构和入口位置。真正建议在平台中安装和发现的统一入口 skill 是：

- `skills/plurk-mcp-skills/SKILL.md`

## 子技能选择

- 统一入口 skill
  读 `skills/plurk-mcp-skills/SKILL.md`
- 查看当前认证账号资料
  读 `skills/plurk-mcp-load-profile/SKILL.md`
- 查看近期 alerts
  读 `skills/plurk-mcp-load-alerts/SKILL.md`
- 查看近期 mentions 或准备回复上下文
  读 `skills/plurk-mcp-load-mentions/SKILL.md`
- 创建新的 plurk
  读 `skills/plurk-mcp-create-post/SKILL.md`
- 回复符合资格的互动
  读 `skills/plurk-mcp-create-reply/SKILL.md`

## 共享参考

在进入具体子技能前，必要时可以先读这些共享资料：

- `skills/_shared/plurk-mcp-contract.md`
- `skills/_shared/plurk-mcp-guardrails.md`
- `skills/_shared/plurk-mcp-workflows.md`

## 记住

- `plurk-mcp` 是执行层，不是内容策略层。
- 不要把未支持动作说成已经可用。
- 涉及实际使用时，优先安装或调用 `skills/` 下的子 skill，而不是直接依赖这个仓库级说明文件。
