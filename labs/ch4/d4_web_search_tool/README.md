# Lab 4.4 — Built-in web search

**Pairs with:** Claude Platform 101 → Built-in tools

## Task
1. `search_answer(question) -> (text, citations)` using the server tool `{"type": "web_search_20250305", "name": "web_search", "max_uses": 3}`; collect `citations` from text blocks (each has `url` and `title`).
2. `SERVER_VS_CLIENT` — a dict with keys `client_tool`, `server_tool` each mapping to a one-line definition (who executes it).

## Exam angles
- Server tools (web search, web fetch, code execution) run on Anthropic's side — no `tool_result` from you; you still see `server_tool_use` and `web_search_tool_result` blocks and pay per search.
- Client tools: you execute and send `tool_result`. `max_uses` caps cost.
