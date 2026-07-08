from pathlib import Path

from tools.repository_integrity.checks import run_repository_integrity_checks


def main() -> int:
    report = run_repository_integrity_checks(Path.cwd())
    output_path = Path("docs/reports/repository-integrity-report.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report.to_markdown(), encoding="utf-8")

    print(report.to_markdown())
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
