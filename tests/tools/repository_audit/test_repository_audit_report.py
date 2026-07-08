from pathlib import Path

from tools.repository_audit.audit import RepositoryAuditReport


def test_repository_audit_report_to_markdown(tmp_path: Path):
    report = RepositoryAuditReport(root=tmp_path)
    report.add_issue("EMPTY_PACKAGE", "package", "Empty")

    markdown = report.to_markdown()

    assert "Repository Audit Report" in markdown
    assert "EMPTY_PACKAGE" in markdown
