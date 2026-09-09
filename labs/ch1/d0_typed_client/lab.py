from common import MODEL, client, aclient

def ask(prompt: str, system: str = "", model: str = MODEL, max_tokens: int = 300):
    """Return the Message object for a single user turn."""
    # TODO: build kwargs; only pass system when it is non-empty
    raise NotImplementedError

async def ask_async(prompt: str, system: str = "", model: str = MODEL, max_tokens: int = 300):
    # TODO: same with the async client (await aclient().messages.create(...))
    raise NotImplementedError

def top_level_keys(message) -> list[str]:
    # TODO: sorted(message.model_dump().keys())
    raise NotImplementedError

if __name__ == "__main__":
    m = ask("Say hello in five words.")
    print(m.content[0].text, m.stop_reason, m.usage)
