from pathlib import Path

from tools.ci_stabilization.checks import run_ci_stabilization_checks


def main() -> int:
    report = run_ci_stabilization_checks(Path.cwd())
    output_path = Path("docs/reports/ci-stabilization-report.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report.to_markdown(), encoding="utf-8")

    print(report.to_markdown())
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
