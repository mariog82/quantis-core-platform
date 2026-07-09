from pathlib import Path
<<<<<<< HEAD
=======

>>>>>>> origin/develop
from tools.test_integrity.checks import run_test_integrity_checks


def main() -> int:
<<<<<<< HEAD
    missing = run_test_integrity_checks(Path.cwd())
    report = Path("docs/reports/test-integrity-report.md")
    report.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Test Integrity Report", "", f"Status: `{'PASS' if not missing else 'FAIL'}`", ""]
    lines.extend(f"- Missing `{item}`" for item in missing)
    report.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 0 if not missing else 1
=======
    report = run_test_integrity_checks(Path.cwd())
    output_path = Path("docs/reports/test-integrity-report.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report.to_markdown(), encoding="utf-8")

    print(report.to_markdown())
    return 0 if report.passed else 1
>>>>>>> origin/develop


if __name__ == "__main__":
    raise SystemExit(main())
