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
    def milestone_doc_name(self) -> str:
        if self.value.startswith("0.5.1-alpha.7"):
            return "M5_1_1_REPOSITORY_RECOVERY.md"
        return "M5_1_RELEASE.md"


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

        lines.extend(["## Issues", ""])
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — `{issue.path}` — {issue.message}")
        return "\n".join(lines)


ReleaseVersion.__test__ = False
ReleaseManagerIssue.__test__ = False
ReleaseManagerReport.__test__ = False


def run_release_manager_checks(root: Path | str = ".") -> ReleaseManagerReport:
    repo_root = Path(root).resolve()
    report = ReleaseManagerReport(root=repo_root)
    version_file = repo_root / "VERSION"

    if not version_file.exists():
        report.add_issue("MISSING_VERSION", "VERSION", "VERSION file is missing.")
        return report

    version = ReleaseVersion(version_file.read_text(encoding="utf-8").strip())
    report.version = version.value

    if not version.valid:
        report.add_issue("INVALID_VERSION", "VERSION", f"`{version.value}` is not SemVer-like.")
        return report

    for file_name in ["CHANGELOG.md", "README.md", "ROADMAP.md"]:
        path = repo_root / file_name
        if not path.exists():
            report.add_issue("MISSING_RELEASE_FILE", file_name, "Required release metadata file is missing.")
        elif version.value not in path.read_text(encoding="utf-8"):
            report.add_issue("VERSION_NOT_REFERENCED", file_name, f"`{version.value}` is not referenced.")

    release_doc = repo_root / "docs" / "release" / version.milestone_doc_name
    if not release_doc.exists():
        report.add_issue("MISSING_RELEASE_DOC", str(release_doc.relative_to(repo_root)), "Release doc missing.")
    elif version.value not in release_doc.read_text(encoding="utf-8"):
        report.add_issue("VERSION_NOT_REFERENCED", str(release_doc.relative_to(repo_root)), "Version not referenced.")

    return report
