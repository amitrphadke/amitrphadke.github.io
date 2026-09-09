from common import MODEL, client

def _ask(prompt: str, max_tokens: int = 300) -> str:
    return client().messages.create(model=MODEL, max_tokens=max_tokens, messages=[{"role": "user", "content": prompt}]).content[0].text

def outline(topic: str) -> str:
    # TODO
    raise NotImplementedError

def ok_outline(text: str) -> bool:
    lines = [l for l in text.strip().splitlines() if l.strip()]
    return len(lines) == 3 and all(l.lstrip().startswith("-") for l in lines)

def draft(outline_text: str) -> str:
    raise NotImplementedError

def polish(draft_text: str) -> str:
    raise NotImplementedError

def chain(topic: str) -> dict:
    chain.retries = 0
    # TODO
    raise NotImplementedError
