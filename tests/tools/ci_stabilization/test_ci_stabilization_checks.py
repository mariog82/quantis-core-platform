from pathlib import Path

from tools.ci_stabilization import run_ci_stabilization_checks


def _write_workflow(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        '''
name: test
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: python -m pip install pytest ruff
      - run: python -m ruff check .
      - run: python -m tools.repository_integrity.cli
      - run: python -m tools.test_integrity.cli
      - run: python -m tools.public_api_integrity.cli
      - run: python -m pytest tests
''',
        encoding="utf-8",
    )


def test_ci_stabilization_passes_when_workflows_exist(tmp_path: Path):
    _write_workflow(tmp_path / ".github/workflows/ci.yml")
    _write_workflow(tmp_path / ".github/workflows/m5-1-ci-stabilization.yml")

    report = run_ci_stabilization_checks(tmp_path)

    assert report.passed is True
    assert report.issues == []


def test_ci_stabilization_detects_missing_workflow(tmp_path: Path):
    _write_workflow(tmp_path / ".github/workflows/ci.yml")

    report = run_ci_stabilization_checks(tmp_path)

    assert report.passed is False
    assert any(issue.code == "MISSING_WORKFLOW" for issue in report.issues)


def test_ci_stabilization_detects_missing_pattern(tmp_path: Path):
    workflow = tmp_path / ".github/workflows/ci.yml"
    workflow.parent.mkdir(parents=True, exist_ok=True)
    workflow.write_text("name: incomplete\n", encoding="utf-8")
    _write_workflow(tmp_path / ".github/workflows/m5-1-ci-stabilization.yml")

    report = run_ci_stabilization_checks(tmp_path)

    assert report.passed is False
    assert any(issue.code == "MISSING_CI_PATTERN" for issue in report.issues)
