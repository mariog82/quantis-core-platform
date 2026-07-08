from dataclasses import dataclass, field
from importlib import import_module
from pathlib import Path
from typing import Any


PUBLIC_PACKAGES = [
    "framework.adapters",
    "framework.adapters.http",
    "framework.adapters.database",
    "framework.adapters.auth",
    "framework.adapters.storage",
    "framework.adapters.messaging",
    "framework.adapters.ai",
    "framework.adapters.notification",
    "framework.adapters.payment",
    "framework.adapters.identity",
    "framework.adapters.sdk",
    "sdk",
    "sdk.generator",
    "tools.repository_integrity",
    "tools.test_integrity",
    "tools.public_api_integrity",
    "tools.ci_stabilization",
    "tools.release_manager",
    "tools.repository_audit",
]

REQUIRED_PUBLIC_SYMBOLS = {
    "framework.adapters": ["Adapter", "AdapterContext", "AdapterMetadata", "AdapterResult"],
    "sdk": ["QuantisClient", "SDKConfig", "SDKResponse"],
    "sdk.generator": ["OpenAPISpec", "SDKManifest"],
    "tools.repository_integrity": ["run_repository_integrity_checks"],
    "tools.test_integrity": ["run_test_integrity_checks"],
    "tools.public_api_integrity": ["run_public_api_integrity_checks"],
    "tools.ci_stabilization": ["run_ci_stabilization_checks"],
    "tools.release_manager": ["run_release_manager_checks"],
    "tools.repository_audit": ["run_repository_audit"],
}


@dataclass(frozen=True)
class APIIssue:
    code: str
    package: str
    message: str


@dataclass
class APIReport:
    root: Path
    issues: list[APIIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def add_issue(self, code: str, package: str, message: str) -> None:
        self.issues.append(APIIssue(code, package, message))

    def to_markdown(self) -> str:
        lines = [
            "# Public API Integrity Report",
            "",
            f"Root: `{self.root}`",
            f"Status: `{'PASS' if self.passed else 'FAIL'}`",
            "",
        ]
        if self.passed:
            lines.append("No public API integrity issues found.")
            return "\n".join(lines)

        lines.extend(["## Issues", ""])
        for issue in self.issues:
            lines.append(f"- `{issue.code}` — `{issue.package}` — {issue.message}")
        return "\n".join(lines)


APIIssue.__test__ = False
APIReport.__test__ = False
PublicAPIIntegrityIssue = APIIssue
PublicAPIIntegrityReport = APIReport
PublicAPIIntegrityIssue.__test__ = False
PublicAPIIntegrityReport.__test__ = False


def _has_all(module: Any) -> bool:
    return hasattr(module, "__all__") and bool(getattr(module, "__all__"))


def _public_symbols_exist(module: Any) -> list[str]:
    return [symbol for symbol in list(getattr(module, "__all__", [])) if not hasattr(module, symbol)]


def run_public_api_integrity_checks(root: Path | str = ".") -> APIReport:
    repo_root = Path(root).resolve()
    report = APIReport(root=repo_root)

    for package_name in PUBLIC_PACKAGES:
        try:
            module = import_module(package_name)
        except ModuleNotFoundError as exc:
            report.add_issue("PACKAGE_NOT_IMPORTABLE", package_name, str(exc))
            continue

        if not _has_all(module):
            report.add_issue("MISSING_ALL", package_name, "Package does not define non-empty __all__.")
            continue

        for symbol in _public_symbols_exist(module):
            report.add_issue("BROKEN_EXPORT", package_name, f"`{symbol}` is listed in __all__ but missing.")

    for package_name, symbols in REQUIRED_PUBLIC_SYMBOLS.items():
        try:
            module = import_module(package_name)
        except ModuleNotFoundError:
            continue

        for symbol in symbols:
            if not hasattr(module, symbol):
                report.add_issue("MISSING_REQUIRED_SYMBOL", package_name, f"`{symbol}` is missing.")

    return report
