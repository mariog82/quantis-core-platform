from pathlib import Path
from tools.ci_stabilization.checks import run_ci_stabilization_checks


def main() -> int:
    issues = run_ci_stabilization_checks(Path.cwd())
    report = Path("docs/reports/ci-stabilization-report.md")
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# CI Stabilization Report", "", f"Status: `{'PASS' if not issues else 'FAIL'}`", ""]
    lines.extend(f"- {item}" for item in issues)
    report.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
