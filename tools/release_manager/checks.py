from dataclasses import dataclass, field
from pathlib import Path
import re


@dataclass(frozen=True)
class ReleaseVersion:
    value: str

    @property
    def valid(self) -> bool:
        return re.match(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$", self.value) is not None

    @property
    def milestone_doc_name(self) -> str:
        if self.value == "0.5.1":
            return "M5_3_STABLE.md"
        if self.value == "0.5.1-rc.1":
            return "M5_2_RELEASE_CANDIDATE.md"
        if self.value == "0.5.1-beta.1":
            return "M5_1_BETA_FREEZE.md"
        return "M5_RELEASE.md"


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
        lines = ["# Release Manager Report", "", f"Status: `{'PASS' if self.passed else 'FAIL'}`", ""]
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

    for metadata_file in ["README.md", "CHANGELOG.md", "ROADMAP.md"]:
        path = repo_root / metadata_file
        if not path.exists():
            report.add_issue("MISSING_RELEASE_METADATA", metadata_file, "Required release metadata file is missing.")
        elif version.value not in path.read_text(encoding="utf-8"):
            report.add_issue("VERSION_NOT_REFERENCED", metadata_file, f"`{version.value}` is not referenced.")

    release_doc = repo_root / "docs" / "release" / version.milestone_doc_name
    if not release_doc.exists():
        report.add_issue("MISSING_RELEASE_DOC", release_doc.as_posix(), "Release doc missing.")
    elif version.value not in release_doc.read_text(encoding="utf-8"):
        report.add_issue("VERSION_NOT_REFERENCED", release_doc.as_posix(), f"`{version.value}` is not referenced.")

    return report
