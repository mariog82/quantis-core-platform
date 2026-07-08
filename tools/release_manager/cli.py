from pathlib import Path

from tools.release_manager.checks import run_release_manager_checks


def main() -> int:
    report = run_release_manager_checks(Path.cwd())
    output_path = Path("docs/reports/release-manager-report.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report.to_markdown(), encoding="utf-8")

    print(report.to_markdown())
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
