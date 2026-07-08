from pathlib import Path

from tools.repository_integrity import run_repository_integrity_checks


def _complete_repo(root: Path) -> None:
    for package in [
        "framework", "framework/adapters", "framework/adapters/http",
        "framework/adapters/database", "framework/adapters/auth",
        "framework/adapters/storage", "framework/adapters/messaging",
        "framework/adapters/ai", "framework/adapters/notification",
        "framework/adapters/payment", "framework/adapters/identity",
        "framework/adapters/sdk", "sdk", "sdk/generator",
    ]:
        path = root / package
        path.mkdir(parents=True, exist_ok=True)
        (path / "__init__.py").write_text("__all__ = ['ok']\nok = object()\n", encoding="utf-8")
    for file in ["VERSION", "README.md", "CHANGELOG.md", "ROADMAP.md", "docs/release/M5_BETA_FREEZE.md"]:
        path = root / file
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("0.5.0-beta.1", encoding="utf-8")


def test_repository_integrity_passes_for_complete_repo(tmp_path: Path):
    _complete_repo(tmp_path)

    report = run_repository_integrity_checks(tmp_path)

    assert report.passed is True


def test_repository_integrity_detects_namespace_package(tmp_path: Path):
    (tmp_path / "framework").mkdir(parents=True)

    report = run_repository_integrity_checks(tmp_path)

    assert any(issue.code == "MISSING_INIT" for issue in report.issues)
