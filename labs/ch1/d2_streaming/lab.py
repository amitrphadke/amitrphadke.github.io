from typing import Iterator
from common import MODEL, client

def stream_text(prompt: str, max_tokens: int = 200) -> Iterator[str]:
    # TODO: with client().messages.stream(...) as s: yield from s.text_stream
    raise NotImplementedError

def stream_with_events(prompt: str, max_tokens: int = 200):
    types: list[str] = []
    # TODO: iterate `for ev in stream:` collecting ev.type, then final = stream.get_final_message()
    raise NotImplementedError

if __name__ == "__main__":
    for chunk in stream_text("Count from one to twenty in words."):
        print(chunk, end="", flush=True)
    print()
