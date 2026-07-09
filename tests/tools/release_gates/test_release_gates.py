from pathlib import Path
from tools.release_gates import run_release_gate_checks


def test_release_gate_checks_pass_for_expected_structure(tmp_path: Path):
    current = tmp_path / "tests/release/current"
    history = tmp_path / "tests/release/history"
    current.mkdir(parents=True)
    history.mkdir(parents=True)
    (current / "test_current.py").write_text("def test_current():\n    assert True\n", encoding="utf-8")
    report = run_release_gate_checks(tmp_path)
    assert report.passed is True


def test_release_gate_checks_detect_missing_current_dir(tmp_path: Path):
    (tmp_path / "tests/release/history").mkdir(parents=True)
    report = run_release_gate_checks(tmp_path)
    assert any(issue.code == "MISSING_CURRENT_RELEASE_GATES" for issue in report.issues)
