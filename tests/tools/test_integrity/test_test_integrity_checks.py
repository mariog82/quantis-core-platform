from pathlib import Path

from tools.test_integrity import run_test_integrity_checks


def _create_minimal_test_tree(root: Path) -> None:
    for directory in [
        "tests/core",
        "tests/framework",
        "tests/framework/adapters",
        "tests/framework/adapters/stabilization",
        "tests/modules",
        "tests/services",
        "tests/sdk",
        "tests/tools",
        "tests/tools/repository_integrity",
    ]:
        test_dir = root / directory
        test_dir.mkdir(parents=True, exist_ok=True)
        (test_dir / "test_placeholder.py").write_text(
            "def test_placeholder():\n    assert True\n",
            encoding="utf-8",
        )


def test_test_integrity_passes_for_complete_test_tree(tmp_path: Path):
    _create_minimal_test_tree(tmp_path)

    for source_dir in [
        "framework/adapters",
        "sdk",
        "tools/repository_integrity",
    ]:
        (tmp_path / source_dir).mkdir(parents=True, exist_ok=True)

    report = run_test_integrity_checks(tmp_path)

    assert report.passed is True
    assert report.issues == []


def test_test_integrity_detects_pycache_only_test_directory(tmp_path: Path):
    _create_minimal_test_tree(tmp_path)
    target = tmp_path / "tests/sdk"
    for child in target.iterdir():
        child.unlink()
    (target / "__pycache__").mkdir()

    report = run_test_integrity_checks(tmp_path)

    assert report.passed is False
    assert any(issue.code == "PYCACHE_ONLY_TEST_DIRECTORY" for issue in report.issues)


def test_test_integrity_detects_missing_test_files_for_public_source(tmp_path: Path):
    _create_minimal_test_tree(tmp_path)
    source = tmp_path / "sdk"
    source.mkdir(parents=True, exist_ok=True)

    for test_file in (tmp_path / "tests/sdk").glob("test_*.py"):
        test_file.unlink()

    report = run_test_integrity_checks(tmp_path)

    assert report.passed is False
    assert any(issue.code == "MISSING_TEST_FILES" for issue in report.issues)
