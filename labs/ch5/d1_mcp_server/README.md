# Lab 5.1 — Your first MCP server (stdio)

**Pairs with:** Introducing MCP → Defining prompts. Runs offline (no API key).
**Needs:** `pip install "mcp[cli]"`.

## Task
In `server.py` with `FastMCP("gitlog")`:
1. tool `git_log(path: str, n: int = 5) -> str` — last n commit subjects of a repo (`git log --oneline -n`).
2. resource `repo://readme` — contents of this lab's README.
3. prompt `summarise_commits(n: int = 5)` — a prompt template asking to summarise the last n commits.
The tests connect to the server over **stdio** with the official client and call all three.

## Exam angles
- Host ↔ client ↔ server; JSON-RPC 2.0; `initialize` → capability negotiation → `tools/list`, `tools/call`, `resources/read`, `prompts/get`.
- Control: tools are **model**-controlled, resources **application**-controlled, prompts **user**-controlled.
- stdio = local child process; Streamable HTTP = remote.
