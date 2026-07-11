from pathlib import Path
from tools.release_gates.checks import run_release_gate_checks


def main() -> int:
    report = run_release_gate_checks(Path.cwd())
    output = Path("docs/reports/release-gates-report.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report.to_markdown(), encoding="utf-8")
    print(report.to_markdown())
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
