from pathlib import Path

from tools.test_integrity.checks import TestIntegrityReport


def test_test_integrity_report_to_markdown_pass(tmp_path: Path):
    report = TestIntegrityReport(root=tmp_path)

    markdown = report.to_markdown()

    assert "Test Integrity Report" in markdown
    assert "PASS" in markdown


def test_test_integrity_report_to_markdown_fail(tmp_path: Path):
    report = TestIntegrityReport(root=tmp_path)
    report.add_issue("EMPTY_TEST_DIRECTORY", "tests/sdk", "No tests")

    markdown = report.to_markdown()

    assert "FAIL" in markdown
    assert "EMPTY_TEST_DIRECTORY" in markdown
