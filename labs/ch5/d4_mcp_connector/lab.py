from common import MODEL, client

SERVER_URL = "https://mcp.deepwiki.com/mcp"
DECISION_RULE = "TODO: when a plain client tool is enough, and when an MCP server pays off (reuse across hosts, standard discovery, remote services)."

def mcp_request(question: str, server_url: str = SERVER_URL, name: str = "deepwiki"):
    # TODO: client().beta.messages.create(model=MODEL, max_tokens=400, messages=[...], mcp_servers=[...], betas=["mcp-client-2025-04-04"])
    raise NotImplementedError

def ask_remote(question: str) -> str:
    m = mcp_request(question)
    return "".join(b.text for b in m.content if getattr(b, "type", "") == "text")
