from common import MODEL, client, PRICES

def estimate(model: str, input_tokens: int, output_tokens: int, cache_read: int = 0, cache_write: int = 0) -> float:
    # TODO
    raise NotImplementedError

def count(messages: list[dict], system: str | None = None, model: str = MODEL) -> int:
    # TODO: client().messages.count_tokens(...).input_tokens
    raise NotImplementedError

def scenarios(calls: int = 1000, inp: int = 10_000, out: int = 500) -> list[dict]:
    # TODO: four rows: {"name", "model", "usd"}; for cached rows 90% of inp is cache_read and the other 10% is normal input
    raise NotImplementedError
