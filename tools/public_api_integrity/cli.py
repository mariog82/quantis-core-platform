from pathlib import Path
from tools.public_api_integrity.checks import run_public_api_integrity_checks


def main() -> int:
    issues = run_public_api_integrity_checks(Path.cwd())
    report = Path("docs/reports/public-api-integrity-report.md")
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Public API Integrity Report", "", f"Status: `{'PASS' if not issues else 'FAIL'}`", ""]
    lines.extend(f"- {item}" for item in issues)
    report.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
