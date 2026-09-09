import pytest
from pathlib import Path
pytest.importorskip("mcp")
import lab
from lab import _check_path, git_log, read_file, ALLOWED_ROOTS

def test_paths_outside_roots_rejected():
    for bad in ["/etc", str(ALLOWED_ROOTS[0] / ".." / ".."), "/tmp; rm -rf /", "../../x"]:
        with pytest.raises(ValueError): _check_path(bad)
    assert _check_path(str(ALLOWED_ROOTS[0])) == ALLOWED_ROOTS[0]

def test_n_validated():
    with pytest.raises(ValueError): git_log(str(ALLOWED_ROOTS[0]), 0)
    with pytest.raises(ValueError): git_log(str(ALLOWED_ROOTS[0]), 500)

def test_read_file_wrapped_and_limited():
    out = read_file("ch5/d5_mcp_hardening/README.md")
    assert out.startswith("<untrusted_file>") and out.rstrip().endswith("</untrusted_file>")
    with pytest.raises(ValueError): read_file("ch5/d5_mcp_hardening/lab.py")
    with pytest.raises(ValueError): read_file("../secret.md")
