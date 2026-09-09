from pathlib import Path
from common import MODEL, client

def big_system() -> str:
    text = (Path(__file__).parent / "policy.txt").read_text()
    return (text + "\n") * 6   # ~5k tokens

def ask_cached(question: str, max_tokens: int = 60):
    # TODO: system=[{"type":"text","text":big_system(),"cache_control":{"type":"ephemeral"}}]
    raise NotImplementedError

def cache_report(m) -> dict:
    u = m.usage
    return {"cache_creation_input_tokens": getattr(u, "cache_creation_input_tokens", 0) or 0,
            "cache_read_input_tokens": getattr(u, "cache_read_input_tokens", 0) or 0,
            "input_tokens": u.input_tokens}

if __name__ == "__main__":
    for q in ["What is the refund window?", "Who approves discounts over 20%?"]:
        print(cache_report(ask_cached(q)))
