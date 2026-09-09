# Lab 4.2 — Agent SDK quickstart (runs on your Claude Code / Max login, no API key)

**Pairs with:** Claude Platform 101 → The agent loop explained · Built-in tools
**Needs:** `pip install claude-agent-sdk` and Claude Code installed and logged in (`claude` on PATH).

## Task
1. `summarise_repo(path) -> str` — `query(prompt=..., options=ClaudeAgentOptions(cwd=path, allowed_tools=["Read","Glob","Grep"], permission_mode="bypassPermissions", max_turns=6))`; collect the final `ResultMessage.result`.
2. `tools_used(path) -> set[str]` — the names of tools the agent actually called (look at `AssistantMessage` content blocks of type `ToolUseBlock`).
3. Write three things the SDK gives you for free (vs. your Chapter 2 loop) in `WHAT_SDK_ADDS` (list of 3 strings).

## Exam angles
- The SDK *is* Claude Code's loop as a library: built-in tools, permissions, context compaction, CLAUDE.md, MCP, subagents, hooks.
- Use the raw Messages API when you need full control or a non-file-system agent; use the SDK for coding/ops agents.
