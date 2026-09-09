# Lab 5.4 — MCP connector (remote MCP from the Messages API)

**Pairs with:** MCP Advanced Topics → StreamableHTTP lessons

## Task
1. `mcp_request(question, server_url, name) -> dict` — build the request body with `mcp_servers=[{"type":"url","url":server_url,"name":name}]` and the beta header `anthropic-beta: mcp-client-2025-04-04` (via `client.beta.messages.create`). Return the raw message.
2. `ask_remote(question)` — use a public demo server (`SERVER_URL` in the file — the DeepWiki server `https://mcp.deepwiki.com/mcp` works without auth) and return the text.
3. `DECISION_RULE` — one paragraph: when to use a plain tool vs. an MCP server.

## Exam angles
- The API can call **remote** (URL) MCP servers for you — stdio servers are for local hosts like Claude Code.
- Tool naming: the server's tools appear as `mcp_tool_use` / `mcp_tool_result` blocks; you can restrict with `tool_configuration.allowed_tools`.
