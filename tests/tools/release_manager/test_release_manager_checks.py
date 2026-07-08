from pathlib import Path

from tools.release_manager import run_release_manager_checks
from tools.release_manager.checks import ReleaseVersion


def _create_release_repo(root: Path, version: str = "0.5.1-alpha.5") -> None:
    (root / "docs/release").mkdir(parents=True, exist_ok=True)
    (root / "VERSION").write_text(version, encoding="utf-8")
    (root / "CHANGELOG.md").write_text(version, encoding="utf-8")
    (root / "README.md").write_text(version, encoding="utf-8")
    (root / "ROADMAP.md").write_text(version, encoding="utf-8")
    (root / "docs/release/M5_1_ALPHA_5.md").write_text(version, encoding="utf-8")


def test_release_version_accepts_semver_prerelease():
    version = ReleaseVersion("0.5.1-alpha.5")

    assert version.valid is True
    assert version.milestone_doc_name == "M5_1_ALPHA_5.md"


def test_release_manager_passes_for_consistent_release(tmp_path: Path):
    _create_release_repo(tmp_path)

    report = run_release_manager_checks(tmp_path)

    assert report.passed is True
    assert report.issues == []


def test_release_manager_detects_missing_version(tmp_path: Path):
    report = run_release_manager_checks(tmp_path)

    assert report.passed is False
    assert any(issue.code == "MISSING_VERSION" for issue in report.issues)


def test_release_manager_detects_invalid_version(tmp_path: Path):
    (tmp_path / "VERSION").write_text("invalid-version", encoding="utf-8")

    report = run_release_manager_checks(tmp_path)

    assert report.passed is False
    assert any(issue.code == "INVALID_VERSION" for issue in report.issues)


def test_release_manager_detects_missing_release_doc(tmp_path: Path):
    _create_release_repo(tmp_path)
    (tmp_path / "docs/release/M5_1_ALPHA_5.md").unlink()

    report = run_release_manager_checks(tmp_path)

    assert report.passed is False
    assert any(issue.code == "MISSING_RELEASE_DOC" for issue in report.issues)
