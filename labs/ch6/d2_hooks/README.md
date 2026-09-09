# Lab 6.2 — Hooks and permission modes

**Pairs with:** Claude Code 101 → Hooks · Claude Code in Action → Hooks, Permission modes. Offline.

## Task
1. `project/.claude/settings.json` with:
   - a `PostToolUse` hook matching `Edit|Write` that runs `hooks/lint.sh`.
   - a `PreToolUse` hook matching `Bash` that runs `hooks/guard.py`.
2. `project/hooks/guard.py` — reads the hook JSON from stdin; if `tool_input.command` contains `rm -rf` or `git push --force`, print a reason to **stderr** and exit **2** (block); otherwise exit 0.
3. `MODES` in `lab.py` — the four permission modes with a one-line meaning each.

## Exam angles
- Exit 0 = allow (stdout shown to model), exit 2 = **block** and feed stderr back to Claude; other codes = non-blocking error.
- Events: `PreToolUse`, `PostToolUse`, `Notification`, `Stop`, `SubagentStop`, `SessionStart`, `UserPromptSubmit`…
- Modes: `default` (ask), `acceptEdits`, `plan` (read-only), `bypassPermissions` (sandboxes/CI only).
