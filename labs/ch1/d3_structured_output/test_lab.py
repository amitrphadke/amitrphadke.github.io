import pytest
from common import has_key
from lab import via_instruction, via_tool, extract_person, Person
pytestmark = pytest.mark.skipif(not has_key(), reason="ANTHROPIC_API_KEY not set")
TEXT = "Priya is a 31-year-old architect who moved to Bengaluru last spring."

def test_tool_route_validates():
    p = via_tool(TEXT)
    assert isinstance(p, Person) and p.name.startswith("Priya") and p.age == 31 and "Bengaluru" in p.city

def test_instruction_route_validates():
    p = via_instruction(TEXT)
    assert p.age == 31

def test_ten_out_of_ten():
    for _ in range(10):
        assert extract_person(TEXT).age == 31
