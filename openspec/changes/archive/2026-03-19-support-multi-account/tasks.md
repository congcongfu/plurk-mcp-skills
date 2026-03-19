## 1. Update Shared References

- [x] 1.1 Rewrite `skills/_shared/plurk-mcp-contract.md` so it documents request-scoped credentials and the supported tool inputs without implying a startup-bound single account.
- [x] 1.2 Update `skills/_shared/plurk-mcp-guardrails.md` and `skills/_shared/plurk-mcp-workflows.md` to describe per-account quota/cooldown isolation and the profile-first confirmation flow for ambiguous multi-account requests.

## 2. Update Skill Workflows

- [x] 2.1 Update `skills/plurk-mcp-skills/SKILL.md` and `skills/plurk-mcp-load-profile/SKILL.md` so they route or confirm the target account for a supplied credentials bundle before further work.
- [x] 2.2 Update `skills/plurk-mcp-load-alerts/SKILL.md` and `skills/plurk-mcp-load-mentions/SKILL.md` so read workflows explicitly operate on the selected account without introducing writes.
- [x] 2.3 Update `skills/plurk-mcp-create-post/SKILL.md` and `skills/plurk-mcp-create-reply/SKILL.md` so write workflows lock the target account as well as the content/thread target before calling `plurk_post` or `plurk_reply`.

## 3. Align Metadata And Verify

- [x] 3.1 Update affected `agents/openai.yaml` files so UI metadata no longer implies a single current account.
- [x] 3.2 Search the repository for stale single-account wording, then run `openspec validate support-multi-account` and resolve any issues.
