from pathlib import Path
from tools.test_integrity import run_test_integrity_checks

def test_test_integrity_detects_pycache_only(tmp_path: Path):
    target = tmp_path / "tests/sdk"
    target.mkdir(parents=True)
    (target / "__pycache__").mkdir()
    report = run_test_integrity_checks(tmp_path)
    assert any(issue.code == "PYCACHE_ONLY_TEST_DIRECTORY" for issue in report.issues)
