from lab import diagnose, load_logs, DIAGNOSTIC_CHECKLIST

def test_all_logs_diagnosed():
    for rec in load_logs():
        assert diagnose(rec) == rec["_expected"], rec["_name"]

def test_checklist():
    assert len(DIAGNOSTIC_CHECKLIST) == 6 and "stop_reason" in " ".join(DIAGNOSTIC_CHECKLIST)
