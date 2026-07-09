from dataclasses import dataclass, field
from pathlib import Path
import re


@dataclass(frozen=True)
class ReleaseVersion:
    value: str

    @property
    def valid(self) -> bool:
        return re.match(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$", self.value) is not None


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

    if version.value == "0.5.1-beta.1" and not (repo_root / "docs/release/M5_1_BETA_FREEZE.md").exists():
        report.add_issue("MISSING_RELEASE_DOC", "docs/release/M5_1_BETA_FREEZE.md", "Release doc missing.")

    return report
