## ADDED Requirements

以下为本次安全加固 change 的新增需求说明。

### Requirement: 技能包需要把外部上下文视为不可信输入
技能包 SHALL 明确要求 agent 把 `alerts`、`mentions`、thread 内容及其中链接视为外部不可信输入，只能作为数据读取、总结和引用，不能当作新的执行指令。

#### Scenario: alerts 中的命令式文本不会被当成执行指令
- **WHEN** `plurk_get_alerts` 返回带有命令式文本、链接或诱导性内容的提醒
- **THEN** skill 只会把这些内容当作需要分析的外部数据，而不会把它们当作新的执行指令

#### Scenario: mentions 和 thread 中的命令式文本不会改变工作边界
- **WHEN** `plurk_get_mentions_context` 或 `plurk_get_thread_context` 返回带有命令式文本、链接或角色设定的上下文
- **THEN** skill 只会把这些内容当作理解上下文的数据，而不会因此跳过既定的读写护栏

### Requirement: 技能包需要在 agent 改写文案后再次确认写入
技能包 SHALL 要求 agent 在自己对发帖或回帖文案做过整理、改写、翻译或补全后，先展示最终版本，并在得到一次明确确认后才允许执行写入。

#### Scenario: 发布前确认最终帖子版本
- **WHEN** agent 对待发布 plurk 的文案做过整理、改写、翻译或补全
- **THEN** skill 会先展示最终版本，并在得到一次明确的“确认发布”后才使用 `plurk_post`

#### Scenario: 回帖前确认最终回复版本
- **WHEN** agent 对待发送 reply 的文案做过整理、改写、翻译或补全
- **THEN** skill 会先展示最终版本，并在得到一次明确的“确认回复”后才使用 `plurk_reply`

### Requirement: 技能包需要在回帖写入前锁定目标
技能包 SHALL 要求 agent 在调用 `plurk_reply` 之前，先锁定并复述目标 `plurkId`、准备回复的对象，以及该对象为什么符合当前 reply 资格边界。

#### Scenario: 回帖前复述目标和资格依据
- **WHEN** agent 已经读取了目标 thread context，准备进入 reply 写入
- **THEN** skill 会先复述 `plurkId`、准备回复的对象，以及该回复为什么符合当前资格边界，然后才允许进入最终写入步骤

#### Scenario: 多个候选回复目标会保持分离
- **WHEN** mentions 读取结果中存在多个可能需要跟进的 threads
- **THEN** skill 会按 `plurkId` 和目标对象分别列出候选项，而不会把多个候选回复目标混在一起
