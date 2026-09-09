import time
from common import MODEL, client

def submit(prompts: list[str]) -> str:
    # TODO: requests=[{"custom_id": f"q{i}", "params": {"model": MODEL, "max_tokens": 50, "messages": [...]}}]
    raise NotImplementedError

def wait(batch_id: str, timeout: int = 900, every: int = 10):
    # TODO: poll client().messages.batches.retrieve(batch_id) until processing_status == "ended"
    raise NotImplementedError

def collect(batch_id: str) -> dict:
    out, counts = {}, {"succeeded": 0, "errored": 0, "canceled": 0, "expired": 0}
    # TODO: for r in client().messages.batches.results(batch_id): ...
    collect.counts = counts
    return out

if __name__ == "__main__":
    b = submit([f"What is {i} squared? Number only." for i in range(20)])
    wait(b); print(collect(b), collect.counts)
