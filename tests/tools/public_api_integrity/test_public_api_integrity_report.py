from pathlib import Path

from tools.public_api_integrity.checks import PublicAPIIntegrityReport


def test_public_api_integrity_report_to_markdown_fail(tmp_path: Path):
    report = PublicAPIIntegrityReport(root=tmp_path)
    report.add_issue("MISSING_ALL", "sdk", "No __all__")

    markdown = report.to_markdown()

    assert "FAIL" in markdown
    assert "MISSING_ALL" in markdown
