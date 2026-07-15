from tools.m7_wp1_freeze import run_freeze_checks

def test_repository_freeze_checks_pass():
    report = run_freeze_checks()
    assert report.version == "0.7.0-beta.1"
    assert report.passed is True
    