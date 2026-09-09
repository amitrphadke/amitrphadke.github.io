# Lab 6.1 — Slash command + skill

**Pairs with:** Claude Code 101 → Skills · Introduction to agent skills. Offline.

## Task
In `project/`:
1. `.claude/commands/test.md` — a user-invoked `/test` command that runs the test suite for `$ARGUMENTS` and summarises failures.
2. `.claude/skills/python-standard/SKILL.md` — YAML front-matter with `name` and a `description` that says **when** to use it (that is what triggers it), then the coding standard.
3. `COMPARISON` in `lab.py`: dict with keys `command`, `skill`, `hook`, `subagent`, `mcp` — one line each: *who invokes it* and *what it is for*.

## Exam angles
- Commands: **user**-invoked (`/name`, `$ARGUMENTS`). Skills: **model**-invoked from the description, can bundle files/scripts. Hooks: deterministic shell on events. Subagents: separate context + tool set. MCP: external tools/data.
