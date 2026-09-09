import pytest
from pathlib import Path
from common import has_key
from lab import image_block_from_file, image_block_from_url, pdf_block_from_file, describe
HERE = Path(__file__).parent

def test_block_shapes():
    b = image_block_from_file(HERE/"sample.png")
    assert b["type"] == "image" and b["source"]["type"] == "base64" and b["source"]["media_type"] == "image/png" and len(b["source"]["data"]) > 100
    u = image_block_from_url("https://example.com/x.jpg")
    assert u["source"] == {"type": "url", "url": "https://example.com/x.jpg"}
    p = pdf_block_from_file(HERE/"sample.pdf")
    assert p["type"] == "document" and p["source"]["media_type"] == "application/pdf" and p.get("citations", {}).get("enabled") is True

@pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")
def test_image_and_pdf_requests_succeed():
    a = describe([image_block_from_file(HERE/"sample.png")], "Name the two dominant colours, lowercase, comma separated.")
    assert any(c in a.lower() for c in ["red", "blue", "orange", "navy"])
    b = describe([pdf_block_from_file(HERE/"sample.pdf")], "What exact text is on the page? Reply with just the text.")
    assert "CCDV-F" in b.upper()
