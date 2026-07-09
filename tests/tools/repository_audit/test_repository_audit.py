from pathlib import Path
from tools.repository_audit import run_repository_audit

def test_repository_audit_counts_files(tmp_path: Path):
    (tmp_path / "a.py").write_text("x=1", encoding="utf-8")
    report = run_repository_audit(tmp_path)
    assert report.total_python_files == 1
