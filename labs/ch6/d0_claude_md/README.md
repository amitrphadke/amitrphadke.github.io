# Lab 6.0 — CLAUDE.md that actually helps

**Pairs with:** Claude Code 101 → The CLAUDE.md file · Claude Code in Action → A CLAUDE.md that follows. Offline.

## Task
Create in this folder a mini project layout:
- `project/CLAUDE.md` — sections **Stack**, **Commands** (how to test/lint/run), **Conventions**, **Review checklist**; and an import line `@docs/style.md`.
- `project/docs/style.md` — the imported file (≥ 5 lines).
- `project/.claude/CLAUDE.local.md`-style personal override is *not* committed: add `CLAUDE.local.md` to `project/.gitignore`.
- `PRECEDENCE` in `lab.py`: list the memory files from **highest to lowest** precedence as Claude Code loads them.

## Exam angles
- Hierarchy: managed policy → user (`~/.claude/CLAUDE.md`) → project (`./CLAUDE.md`, committed) → local (`./CLAUDE.local.md`, git-ignored); deeper directories add on top when you work there. `@path` imports, max depth 5.
- Keep it short and imperative; it is loaded into every session's context.
