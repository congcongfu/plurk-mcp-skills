## MODIFIED Requirements

### Requirement: Create Post 技能必须使用受护栏保护的新帖工作流
`plurk-mcp-create-post` 技能 SHALL 指导 agent 起草新 plurk；在 Laike 台湾区公开推广场景下，skill SHALL 先读取本地角色素材、再起草符合指定内容策略且带明确披露的新 plurk，并且仅在最终内容锁定且用户明确要求立即发布后，才将 `plurk_post` 作为创建新帖的唯一写步骤。

#### Scenario: 为 Laike 台湾区生成公开推广草稿
- **WHEN** 用户要求 agent 为 Laike 在 Plurk 上起草或发布一条推广内容
- **THEN** skill 会先进入草稿生成工作流，而不是立即调用 `plurk_post`

#### Scenario: 起草前读取本地角色表
- **WHEN** skill 开始准备 Laike 推广内容
- **THEN** agent 会先读取 workspace 根目录下的 `laike男性角色表.xlsx`，并把其中可用的男性角色信息当作现有角色素材来源

#### Scenario: 本地角色表缺失时不能编造现有角色
- **WHEN** `laike男性角色表.xlsx` 不存在、不可读或当前环境无法成功读取
- **THEN** skill 会明确说明缺少本地角色素材，且不会伪造“表内现有角色”信息

#### Scenario: 推广内容必须明确披露
- **WHEN** agent 为 Laike 生成推广草稿
- **THEN** 文案会清楚表明这是推荐、产品分享、体验分享或合作资讯之一，而不会伪装成普通用户自发心得

#### Scenario: 起草内容必须遵守 Laike 推广策略
- **WHEN** agent 为该 skill 生成 Plurk 草稿
- **THEN** 草稿会使用台湾惯用繁体中文、控制在 20-200 字之间、采用四种内容方向之一随机选题、自然带出 Laike 或邀请码，并在文末附上 1-2 个精准标签

#### Scenario: 需要结合现有角色时引用本地素材
- **WHEN** 随机选到的主题适合结合 Laike 现有角色
- **THEN** skill 会优先使用 `laike男性角色表.xlsx` 中读取到的角色素材，而不是凭空捏造角色设定

#### Scenario: 情绪陪伴与娱乐玩法不能写成保证结果
- **WHEN** 草稿提到聊天陪伴、情绪支持或娱乐向占卜玩法
- **THEN** skill 只会把它们写成功能介绍或体验分享，而不会写成医疗、心理治疗或保证准确的结果

#### Scenario: 发布新的 plurk
- **WHEN** 用户要求 agent 通过 `plurk-mcp` 发布新的 plurk，且最终文案已经锁定
- **THEN** skill 会在最终写入时使用 `plurk_post`

#### Scenario: agent 改写过文案时需要再次确认
- **WHEN** agent 对待发布内容做过整理、改写、翻译、补全，或根据内容方向重新组织过文案
- **THEN** skill 会先展示最终版本，并在得到一次明确确认后才使用 `plurk_post`

#### Scenario: 每日配额阻止新帖发布
- **WHEN** `plurk_post` 因服务端每日新帖配额耗尽而被拒绝
- **THEN** skill 会把这次拒绝当作策略边界进行反馈，而不会建议任何不被支持的绕过行为
