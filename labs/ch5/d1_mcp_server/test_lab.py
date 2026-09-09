import asyncio, sys, pytest
from pathlib import Path
pytest.importorskip("mcp")
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
HERE = Path(__file__).parent

async def _session(fn):
    params = StdioServerParameters(command=sys.executable, args=[str(HERE / "lab.py")])
    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            return await fn(s)

def test_tool_listed_and_callable(tmp_path):
    import subprocess
    r = tmp_path / "repo"; r.mkdir()
    sh = lambda *a: subprocess.run(["git", "-C", str(r), *a], capture_output=True, text=True, check=True)
    sh("init", "-q"); sh("config", "user.email", "t@t"); sh("config", "user.name", "t")
    (r / "a.txt").write_text("x"); sh("add", "-A"); sh("commit", "-qm", "first commit here")
    async def go(s):
        tools = {t.name for t in (await s.list_tools()).tools}
        assert "git_log" in tools
        res = await s.call_tool("git_log", {"path": str(r), "n": 3})
        return res.content[0].text
    out = asyncio.run(_session(go))
    assert "first commit here" in out

def test_resource_and_prompt():
    async def go(s):
        res = await s.list_resources()
        assert any(str(r.uri) == "repo://readme" for r in res.resources)
        body = (await s.read_resource("repo://readme")).contents[0].text
        prompts = {p.name for p in (await s.list_prompts()).prompts}
        assert "summarise_commits" in prompts
        p = await s.get_prompt("summarise_commits", {"n": "3"})
        return body, p.messages[0].content.text
    body, ptext = asyncio.run(_session(go))
    assert "Lab 5.1" in body and "3" in ptext
