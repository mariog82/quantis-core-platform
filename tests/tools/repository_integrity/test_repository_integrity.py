from pathlib import Path
from tools.repository_integrity import run_repository_integrity_checks

def test_repository_integrity_detects_missing_init(tmp_path: Path):
    (tmp_path / "framework").mkdir()
    report = run_repository_integrity_checks(tmp_path)
    assert any(issue.code == "MISSING_INIT" for issue in report.issues)
