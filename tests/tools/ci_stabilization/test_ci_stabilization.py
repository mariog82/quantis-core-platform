from pathlib import Path
from tools.ci_stabilization import run_ci_stabilization_checks

def test_ci_stabilization_detects_missing_workflow(tmp_path: Path):
    report = run_ci_stabilization_checks(tmp_path)
    assert any(issue.code == "MISSING_WORKFLOW" for issue in report.issues)
