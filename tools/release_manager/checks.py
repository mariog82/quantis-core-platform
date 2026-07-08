from dataclasses import dataclass, field
from pathlib import Path
import re


SEMVER_PATTERN = re.compile(
    r"^(?P<major>0|[1-9]\d*)\."
    r"(?P<minor>0|[1-9]\d*)\."
    r"(?P<patch>0|[1-9]\d*)"
    r"(?:-(?P<prerelease>[0-9A-Za-z.-]+))?$"
)


@dataclass(frozen=True)
class ReleaseVersion:
    value: str

    @property
    def valid(self) -> bool:
        return SEMVER_PATTERN.match(self.value) is not None

    @property
    def release_doc_name(self) -> str:
        normalized = self.value.upper().replace(".", "_").replace("-", "_")
        return f"RELEASE_{normalized}.md"

    @property
    def milestone_doc_name(self) -> str:
        if self.value.startswith("0.5.1-alpha.5"):
            return "M5_1_ALPHA_5.md"
        if self.value.startswith("0.5.1"):
            return "M5_1_RELEASE.md"
        return self.release_doc_name


@dataclass(frozen=True)
class ReleaseManagerIssue:
    code: str
    path: str
    message: str


@dataclass
class ReleaseManagerReport:
    root: Path
    version: str | None = None
    issues: list[ReleaseManagerIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def add_issue(self, code: str, path: str, message: str) -> None:
        self.issues.append(ReleaseManagerIssue(code, path, message))

    def to_markdown(self) -> str:
        lines = [
            "# Release Manager Report",
            "",
            f"Root: `{self.root}`",
            f"Version: `{self.version or 'UNKNOWN'}`",
            f"Status: `{'PASS' if self.passed else 'FAIL'}`",
            "",
        ]

        if self.passed:
            lines.append("No release manager issues found.")
            return "\n".join(lines)

        lines.append("## Issues")
        lines.append("")
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — `{issue.path}` — {issue.message}")

        return "\n".join(lines)


ReleaseVersion.__test__ = False
ReleaseManagerIssue.__test__ = False
ReleaseManagerReport.__test__ = False


def _read_version(repo_root: Path, report: ReleaseManagerReport) -> ReleaseVersion | None:
    version_file = repo_root / "VERSION"
    if not version_file.exists():
        report.add_issue("MISSING_VERSION", "VERSION", "VERSION file is missing.")
        return None

    value = version_file.read_text(encoding="utf-8").strip()
    report.version = value
    version = ReleaseVersion(value=value)

    if not version.valid:
        report.add_issue(
            "INVALID_VERSION",
            "VERSION",
            f"Version `{value}` does not follow SemVer or SemVer prerelease format.",
        )

    return version


def _file_contains(path: Path, expected: str) -> bool:
    return path.exists() and expected in path.read_text(encoding="utf-8")


def _check_version_references(repo_root: Path, version: ReleaseVersion, report: ReleaseManagerReport) -> None:
    for file_name in ["CHANGELOG.md", "README.md", "ROADMAP.md"]:
        path = repo_root / file_name
        if not path.exists():
            report.add_issue("MISSING_RELEASE_FILE", file_name, "Required release metadata file is missing.")
            continue

        if version.value not in path.read_text(encoding="utf-8"):
            report.add_issue(
                "VERSION_NOT_REFERENCED",
                file_name,
                f"Current version `{version.value}` is not referenced.",
            )


def _check_release_docs(repo_root: Path, version: ReleaseVersion, report: ReleaseManagerReport) -> None:
    docs_release = repo_root / "docs" / "release"
    if not docs_release.exists():
        report.add_issue("MISSING_RELEASE_DOCS_DIR", "docs/release", "Release docs directory is missing.")
        return

    milestone_doc = docs_release / version.milestone_doc_name
    if not milestone_doc.exists():
        report.add_issue(
            "MISSING_RELEASE_DOC",
            str(milestone_doc.relative_to(repo_root)),
            "Release documentation for the current version is missing.",
        )
        return

    if version.value not in milestone_doc.read_text(encoding="utf-8"):
        report.add_issue(
            "VERSION_NOT_REFERENCED",
            str(milestone_doc.relative_to(repo_root)),
            f"Release document does not reference `{version.value}`.",
        )


def _check_duplicate_release_docs(repo_root: Path, version: ReleaseVersion, report: ReleaseManagerReport) -> None:
    docs_release = repo_root / "docs" / "release"
    if not docs_release.exists():
        return

    matching_docs = [
        path
        for path in docs_release.glob("*.md")
        if version.value in path.read_text(encoding="utf-8")
    ]

    # The current release may appear in one release note and in a cumulative document.
    if len(matching_docs) > 3:
        report.add_issue(
            "DUPLICATE_RELEASE_REFERENCES",
            "docs/release",
            f"Version `{version.value}` appears in too many release documents.",
        )


def run_release_manager_checks(root: Path | str = ".") -> ReleaseManagerReport:
    repo_root = Path(root).resolve()
    report = ReleaseManagerReport(root=repo_root)

    version = _read_version(repo_root, report)
    if version is None:
        return report

    if version.valid:
        _check_version_references(repo_root, version, report)
        _check_release_docs(repo_root, version, report)
        _check_duplicate_release_docs(repo_root, version, report)

    return report
