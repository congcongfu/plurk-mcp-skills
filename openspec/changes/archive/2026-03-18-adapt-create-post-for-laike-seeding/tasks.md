## 1. Update Create Post Skill

- [x] 1.1 Rewrite `skills/plurk-mcp-create-post/SKILL.md` to add the transparent Laike Taiwan promotion brief, four content directions, and the required output constraints for Plurk drafts.
- [x] 1.2 Add an explicit step in `skills/plurk-mcp-create-post/SKILL.md` to read `laike男性角色表.xlsx` from the workspace root before selecting whether to use an existing role.
- [x] 1.3 Document the fallback behavior in `skills/plurk-mcp-create-post/SKILL.md` for missing or unreadable workbook input, including the rule against fabricating workbook-derived roles.
- [x] 1.4 Preserve the existing publish gate in `skills/plurk-mcp-create-post/SKILL.md` so draft generation stays separate from the final `plurk_post` write, and require transparent disclosure for Laike promotional content.

## 2. Align Agent Metadata

- [x] 2.1 Update `skills/plurk-mcp-create-post/agents/openai.yaml` so the display text and default prompt match the new transparent Laike draft-first workflow.
- [x] 2.2 Ensure the agent metadata still makes the final confirmation and disclosure requirements explicit before any `plurk_post` call.

## 3. Validate Spec And Change Artifacts

- [x] 3.1 Verify the Create Post spec wording stays aligned with the updated transparent-promotion behavior and workbook-handling rules.
- [x] 3.2 Run `openspec validate adapt-create-post-for-laike-seeding` and resolve any validation issues.
