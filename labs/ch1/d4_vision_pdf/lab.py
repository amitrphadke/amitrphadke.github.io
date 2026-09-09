import base64, mimetypes
from pathlib import Path
from common import MODEL, client

def image_block_from_file(path: str) -> dict:
    # TODO
    raise NotImplementedError

def image_block_from_url(url: str) -> dict:
    # TODO
    raise NotImplementedError

def pdf_block_from_file(path: str) -> dict:
    # TODO (document block, application/pdf, citations enabled)
    raise NotImplementedError

def describe(blocks: list[dict], question: str, max_tokens: int = 200) -> str:
    # TODO: one user message with blocks + {"type":"text","text":question}
    raise NotImplementedError

if __name__ == "__main__":
    here = Path(__file__).parent
    print(describe([image_block_from_file(here/"sample.png")], "What colours do you see?"))
