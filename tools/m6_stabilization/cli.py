from pathlib import Path

from tools.m6_stabilization.checks import run_m6_stabilization_checks


def main() -> int:
    report = run_m6_stabilization_checks()

    output = Path("docs/reports/m6-stabilization-report.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report.to_markdown(), encoding="utf-8")

    print(report.to_markdown())
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
