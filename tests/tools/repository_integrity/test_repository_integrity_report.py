from pathlib import Path

from tools.repository_integrity.checks import RepositoryIntegrityReport


def test_repository_integrity_report_markdown(tmp_path: Path):
    report = RepositoryIntegrityReport(root=tmp_path)
    report.add_issue("MISSING_INIT", "framework", "Missing init")

    markdown = report.to_markdown()

    assert "FAIL" in markdown
    assert "MISSING_INIT" in markdown
