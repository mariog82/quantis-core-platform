from pathlib import Path

from tools.repository_audit import run_repository_audit


def test_repository_audit_collects_tree_and_counts(tmp_path: Path):
    (tmp_path / "package").mkdir()
    (tmp_path / "package/__init__.py").write_text("__all__ = []\n", encoding="utf-8")
    (tmp_path / "package/module.py").write_text("VALUE = 1\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("# Demo\n", encoding="utf-8")

    report = run_repository_audit(tmp_path)

    assert report.total_files == 3
    assert report.total_python_files == 2
    assert any(entry.path == "package/module.py" for entry in report.tree)


def test_repository_audit_detects_pycache_only_directory(tmp_path: Path):
    target = tmp_path / "tests/sdk"
    target.mkdir(parents=True)
    (target / "__pycache__").mkdir()

    report = run_repository_audit(tmp_path)

    assert any(issue.code == "PYCACHE_ONLY_DIRECTORY" for issue in report.issues)


def test_repository_audit_detects_large_source_file(tmp_path: Path):
    target = tmp_path / "large.py"
    target.write_text("x" * 500_001, encoding="utf-8")

    report = run_repository_audit(tmp_path)

    assert any(issue.code == "LARGE_SOURCE_FILE" for issue in report.issues)
