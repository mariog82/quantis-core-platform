from pathlib import Path

from tools.release_manager.checks import ReleaseManagerReport


def test_release_manager_report_to_markdown_pass(tmp_path: Path):
    report = ReleaseManagerReport(root=tmp_path, version="0.5.1-alpha.5")

    markdown = report.to_markdown()

    assert "Release Manager Report" in markdown
    assert "PASS" in markdown
    assert "0.5.1-alpha.5" in markdown


def test_release_manager_report_to_markdown_fail(tmp_path: Path):
    report = ReleaseManagerReport(root=tmp_path, version="0.5.1-alpha.5")
    report.add_issue("MISSING_VERSION", "VERSION", "Missing")

    markdown = report.to_markdown()

    assert "FAIL" in markdown
    assert "MISSING_VERSION" in markdown
