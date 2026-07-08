from pathlib import Path

from tools.ci_stabilization.checks import CIStabilizationReport


def test_ci_stabilization_report_to_markdown_pass(tmp_path: Path):
    report = CIStabilizationReport(root=tmp_path)

    markdown = report.to_markdown()

    assert "CI Stabilization Report" in markdown
    assert "PASS" in markdown


def test_ci_stabilization_report_to_markdown_fail(tmp_path: Path):
    report = CIStabilizationReport(root=tmp_path)
    report.add_issue("MISSING_WORKFLOW", ".github/workflows/ci.yml", "Missing")

    markdown = report.to_markdown()

    assert "FAIL" in markdown
    assert "MISSING_WORKFLOW" in markdown
