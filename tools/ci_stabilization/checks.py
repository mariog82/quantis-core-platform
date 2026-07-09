from pathlib import Path


def run_ci_stabilization_checks(root: Path | str = "."):
    repo_root = Path(root).resolve()
    workflow = repo_root / ".github/workflows/ci.yml"
    if not workflow.exists():
        return ["missing .github/workflows/ci.yml"]
    content = workflow.read_text(encoding="utf-8")
    patterns = ["ruff", "pytest"]
    return [f"missing pattern {p}" for p in patterns if p not in content]
