# Lab 6.4 — Headless Claude Code

**Pairs with:** Claude Code in Action → Routines and headless · GitHub Actions and Code Review.
**Needs:** Claude Code installed and logged in (Max).

## Task
1. `run_headless(prompt, cwd) -> dict` — `subprocess.run(["claude","-p",prompt,"--output-format","json","--max-turns","3","--allowedTools","Read,Glob"], cwd=cwd)` and `json.loads` the stdout; return the parsed dict.
2. `result_text(d)` — the `result` field; `cost(d)` — `total_cost_usd`.
3. `workflow.yml` — a GitHub Actions job that, on `pull_request`, runs `claude -p "review this diff"` with `ANTHROPIC_API_KEY` from secrets (file only, not executed).

## Exam angles
- `-p` = non-interactive; `--output-format json|stream-json`; `--allowedTools`, `--max-turns`, `--permission-mode` for CI safety.
- CI uses an API key (or the Claude GitHub app), never a personal login.
