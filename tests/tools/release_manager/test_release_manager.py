from pathlib import Path
from tools.release_manager import run_release_manager_checks

def test_release_manager_detects_missing_version(tmp_path: Path):
    report = run_release_manager_checks(tmp_path)
    assert any(issue.code == "MISSING_VERSION" for issue in report.issues)
