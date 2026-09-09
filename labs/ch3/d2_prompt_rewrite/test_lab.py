import pytest
from common import has_key
from lab import PROMPT_V1, PROMPT_V2, PROMPT_V3, score
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")

def test_versions_improve():
    assert "TODO" not in PROMPT_V2 and "TODO" not in PROMPT_V3
    assert "<" in PROMPT_V3 and ">" in PROMPT_V3, "V3 should use XML tags"
    s1, s2, s3 = score(PROMPT_V1), score(PROMPT_V2), score(PROMPT_V3)
    print(s1, s2, s3)
    assert s3 >= 0.85 and s3 >= s2 - 0.13 and s2 >= s1 - 0.13
