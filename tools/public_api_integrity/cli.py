from pathlib import Path

from tools.public_api_integrity.checks import run_public_api_integrity_checks


def main() -> int:
    report = run_public_api_integrity_checks(Path.cwd())
    output_path = Path("docs/reports/public-api-integrity-report.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report.to_markdown(), encoding="utf-8")

    print(report.to_markdown())
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
