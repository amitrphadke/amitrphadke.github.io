import subprocess
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("gitlog")

@mcp.tool()
def git_log(path: str, n: int = 5) -> str:
    """Last n commit subjects of the git repo at path."""
    # TODO: subprocess.run(["git","-C",path,"log","--oneline",f"-{n}"], capture_output=True, text=True).stdout
    raise NotImplementedError

# TODO: @mcp.resource("repo://readme") def readme() -> str
# TODO: @mcp.prompt() def summarise_commits(n: int = 5) -> str

if __name__ == "__main__":
    mcp.run()   # stdio
