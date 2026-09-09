# Lab 6.3 — Reviewer subagent

**Pairs with:** Claude Code 101 → Subagents · Introduction to subagents. Offline (then try it for real on a PR).

## Task
`project/.claude/agents/reviewer.md` with front-matter `name: reviewer`, a `description` that tells the main agent **when to delegate** (code review, PRs), `tools: Read, Grep, Glob` (read-only), and a system prompt body with a review checklist (≥ 5 items).

## Exam angles
- Subagents run in their **own context window** with their own tools/model; the parent only sees the summary — great for noisy searches and reviews.
- `tools:` restricts capability; omit it to inherit everything.
