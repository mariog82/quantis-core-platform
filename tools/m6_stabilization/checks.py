from dataclasses import dataclass, field
from pathlib import Path
import re


EXPECTED_VERSION = "0.6.0"

REQUIRED_PATHS = (
    "docs/release/M6_FINAL_RELEASE.md",
    "docs/release/M6_FINAL_CHECKLIST.md",
    "docs/release/M6_PUBLIC_API_BASELINE.md",
    "docs/release/M6_MIGRATION_NOTES.md",
    "docs/adr/ADR-085-m6-final-release.md",
    "docs/rfc/RFC-028-m6-final-release.md",
)

CONFLICT_MARKER_PATTERN = re.compile(
    r"^(<<<<<<<(?: .*)?|=======|>>>>>>>(?: .*)?)$",
    re.MULTILINE,
)


@dataclass(frozen=True)
class M6StabilizationIssue:
    code: str
    message: str
    path: str | None = None


@dataclass
class M6StabilizationReport:
    issues: list[M6StabilizationIssue] = field(default_factory=list)
    files_scanned: int = 0
    python_files_scanned: int = 0

    @property
    def passed(self) -> bool:
        return not self.issues

    def add(
        self,
        code: str,
        message: str,
        path: str | None = None,
    ) -> None:
        self.issues.append(
            M6StabilizationIssue(
                code=code,
                message=message,
                path=path,
            )
        )

    def to_markdown(self) -> str:
        lines = [
            "# M6 Stabilization Report",
            "",
            f"Status: `{'PASS' if self.passed else 'FAIL'}`",
            "",
            f"- Files scanned: `{self.files_scanned}`",
            f"- Python files scanned: `{self.python_files_scanned}`",
            "",
        ]

        if self.issues:
            lines.append("## Issues")
            lines.append("")
            for issue in self.issues:
                location = f" — `{issue.path}`" if issue.path else ""
                lines.append(
                    f"- `{issue.code}`: {issue.message}{location}"
                )
        else:
            lines.append("No stabilization issues detected.")

        return "\n".join(lines)


M6StabilizationIssue.__test__ = False
M6StabilizationReport.__test__ = False


def _is_scannable(path: Path) -> bool:
    excluded_parts = {
        ".git",
        ".pytest_cache",
        ".ruff_cache",
        "__pycache__",
        ".venv",
        "venv",
        "node_modules",
        "dist",
        "build",
    }
    return not any(part in excluded_parts for part in path.parts)


def run_m6_stabilization_checks(
    root: Path | str = Path("."),
) -> M6StabilizationReport:
    repository = Path(root)
    report = M6StabilizationReport()

    version_file = repository / "VERSION"
    if not version_file.exists():
        report.add(
            "MISSING_VERSION",
            "VERSION file is missing.",
            "VERSION",
        )
    else:
        version = version_file.read_text(encoding="utf-8").strip()
        if version != EXPECTED_VERSION:
            report.add(
                "INVALID_VERSION",
                f"Expected {EXPECTED_VERSION}, found {version}.",
                "VERSION",
            )

    for required in REQUIRED_PATHS:
        if not (repository / required).exists():
            report.add(
                "MISSING_RELEASE_ARTIFACT",
                "Required M6 release artifact is missing.",
                required,
            )

    public_packages = (
        repository / "core" / "workflow2" / "__init__.py",
        repository / "core" / "event" / "__init__.py",
        repository / "sdk" / "workflow" / "__init__.py",
    )
    for package in public_packages:
        if not package.exists():
            report.add(
                "MISSING_PUBLIC_PACKAGE",
                "Required public package entry point is missing.",
                str(package.relative_to(repository)),
            )

    for path in repository.rglob("*"):
        relative = path.relative_to(repository)

        if not path.is_file() or not _is_scannable(relative):
            continue

        report.files_scanned += 1
        if path.suffix == ".py":
            report.python_files_scanned += 1

        if path.suffix not in {
            ".py",
            ".md",
            ".yml",
            ".yaml",
            ".toml",
            ".ini",
            ".txt",
        }:
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        match = CONFLICT_MARKER_PATTERN.search(content)
        if match is not None:
            report.add(
                "CONFLICT_MARKER",
                f"Unresolved Git conflict marker: {match.group(1)}",
                str(relative),
            )

    return report
