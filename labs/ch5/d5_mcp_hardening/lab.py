import subprocess
from pathlib import Path
from mcp.server.fastmcp import FastMCP

ALLOWED_ROOTS = [Path(__file__).resolve().parents[2]]   # the labs/ folder by default
mcp = FastMCP("gitlog-hardened")

def _check_path(path: str) -> Path:
    # TODO: reject '..', ';', '|', '&', '`', '$'; resolve; ensure it is inside one of ALLOWED_ROOTS
    raise NotImplementedError

@mcp.tool()
def git_log(path: str, n: int = 5) -> str:
    """Last n commit subjects (1-50) of an allowed repo."""
    # TODO
    raise NotImplementedError

@mcp.tool()
def read_file(rel_path: str) -> str:
    """Read a .md/.txt file (max 20 kB) inside the allowed root, wrapped as untrusted data."""
    # TODO
    raise NotImplementedError

if __name__ == "__main__":
    mcp.run()
