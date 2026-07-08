from pathlib import Path

from tools.repository_integrity import run_repository_integrity_checks


def test_repository_integrity_report_passes_for_complete_minimal_repo(tmp_path: Path):
    for package in [
        "framework",
        "framework/adapters",
        "framework/adapters/http",
        "framework/adapters/database",
        "framework/adapters/auth",
        "framework/adapters/storage",
        "framework/adapters/messaging",
        "framework/adapters/ai",
        "framework/adapters/notification",
        "framework/adapters/payment",
        "framework/adapters/identity",
        "framework/adapters/sdk",
        "sdk",
        "sdk/generator",
    ]:
        package_path = tmp_path / package
        package_path.mkdir(parents=True)
        (package_path / "__init__.py").write_text("__all__ = []\n", encoding="utf-8")

    for required_file in [
        "VERSION",
        "README.md",
        "CHANGELOG.md",
        "ROADMAP.md",
        "docs/release/M5_BETA_FREEZE.md",
    ]:
        file_path = tmp_path / required_file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text("ok", encoding="utf-8")

    report = run_repository_integrity_checks(tmp_path)

    assert report.passed is True
    assert report.issues == []


def test_repository_integrity_report_detects_namespace_package(tmp_path: Path):
    package_path = tmp_path / "framework"
    package_path.mkdir(parents=True)

    report = run_repository_integrity_checks(tmp_path)

    assert report.passed is False
    assert any(issue.code == "MISSING_INIT" for issue in report.issues)


def test_repository_integrity_report_detects_pycache_only_package(tmp_path: Path):
    package_path = tmp_path / "framework"
    package_path.mkdir(parents=True)
    (package_path / "__pycache__").mkdir()

    report = run_repository_integrity_checks(tmp_path)

    assert report.passed is False
    assert any(issue.code == "PYCACHE_ONLY_PACKAGE" for issue in report.issues)
