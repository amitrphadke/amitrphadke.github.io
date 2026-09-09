import asyncio
from pathlib import Path

WHAT_SDK_ADDS = [
    # TODO: three strings
]

async def _run(path: str, prompt: str):
    from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage, ToolUseBlock
    used, result = set(), ""
    # TODO: async for msg in query(prompt=prompt, options=ClaudeAgentOptions(...)): collect tool names and the result
    return result, used

def summarise_repo(path: str) -> str:
    return asyncio.run(_run(path, "In three sentences, what is in this directory? Read files as needed."))[0]

def tools_used(path: str) -> set[str]:
    return asyncio.run(_run(path, "List the .py files here and say what the largest one does. Use tools."))[1]
