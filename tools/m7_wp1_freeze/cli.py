from tools.m7_wp1_freeze.checks import run_freeze_checks


def main() -> int:
    report = run_freeze_checks()
    print("# M7 WP1 Freeze Report")
    print()
    print(f"Version: `{report.version}`")
    print(f"Status: `{'PASS' if report.passed else 'FAIL'}`")
    print(f"Required artifacts checked: `{report.checked_files}`")
    if report.issues:
        print()
        print("## Issues")
        for issue in report.issues:
            print(f"- `{issue.code}` Ã¢â‚¬â€ `{issue.path}` Ã¢â‚¬â€ {issue.message}")
    else:
        print()
        print("No freeze issues detected.")
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
