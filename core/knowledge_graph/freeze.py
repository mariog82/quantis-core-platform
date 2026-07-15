from dataclasses import dataclass
from pathlib import Path
import subprocess
from typing import Iterable


@dataclass(frozen=True)
class FreezeIssue:
    code: str
    path: str
    message: str


@dataclass(frozen=True)
class FreezeReport:
    version: str
    checked_files: int
    issues: tuple[FreezeIssue, ...]

    @property
    def passed(self) -> bool:
        return not self.issues


class KnowledgeGraphFreezeValidator:
    def __init__(
        self,
        required_paths: Iterable[str] | None = None,
    ) -> None:
        self.required_paths = tuple(
            required_paths
            or (
                "core/knowledge_graph/graph.py",
                "core/knowledge_graph/entity_registry.py",
                "core/knowledge_graph/relationship_engine.py",
                "core/knowledge_graph/inmemory_repository.py",
                "core/knowledge_graph/query_engine.py",
                "core/knowledge_graph/query_optimizer.py",
                "core/knowledge_graph/graph_algorithms.py",
                "core/knowledge_graph/graph_analytics.py",
                "core/knowledge_graph/semantic_layer.py",
            )
        )

    def validate(
        self,
        root: Path | None = None,
    ) -> FreezeReport:
        repository = (root or Path.cwd()).resolve()
        issues: list[FreezeIssue] = []

        version_path = repository / "VERSION"
        version = (
            version_path.read_text(encoding="utf-8").strip()
            if version_path.exists()
            else "missing"
        )

        self._check_required_paths(repository, issues)
        self._check_git_unmerged_files(repository, issues)
        self._check_git_diff(repository, issues)

        return FreezeReport(
            version=version,
            checked_files=len(self.required_paths),
            issues=tuple(issues),
        )

    def _check_required_paths(
        self,
        repository: Path,
        issues: list[FreezeIssue],
    ) -> None:
        for relative_path in self.required_paths:
            if not (repository / relative_path).exists():
                issues.append(
                    FreezeIssue(
                        code="MISSING_REQUIRED_PATH",
                        path=relative_path,
                        message=(
                            "Required Knowledge Graph artifact is missing."
                        ),
                    )
                )

    def _check_git_unmerged_files(
        self,
        repository: Path,
        issues: list[FreezeIssue],
    ) -> None:
        result = self._run_git(
            repository,
            "ls-files",
            "-u",
        )

        if result.returncode != 0:
            issues.append(
                FreezeIssue(
                    code="GIT_CHECK_FAILED",
                    path=".git",
                    message=result.stderr.strip()
                    or "Unable to inspect unmerged files.",
                )
            )
            return

        unmerged_paths: set[str] = set()

        for line in result.stdout.splitlines():
            parts = line.split(maxsplit=3)
            if len(parts) == 4:
                unmerged_paths.add(parts[3])

        for path in sorted(unmerged_paths):
            issues.append(
                FreezeIssue(
                    code="UNMERGED_FILE",
                    path=path,
                    message="File is still marked as unmerged by Git.",
                )
            )

    def _check_git_diff(
        self,
        repository: Path,
        issues: list[FreezeIssue],
    ) -> None:
        result = self._run_git(
            repository,
            "diff",
            "--check",
            "HEAD",
            "--",
        )

        if result.returncode == 0:
            return

        output = result.stdout.strip() or result.stderr.strip()

        for line in output.splitlines():
            if not line.strip():
                continue

            path = line.split(":", maxsplit=1)[0]

            issues.append(
                FreezeIssue(
                    code="GIT_DIFF_CHECK",
                    path=path,
                    message=line.strip(),
                )
            )

    @staticmethod
    def _run_git(
        repository: Path,
        *arguments: str,
    ) -> subprocess.CompletedProcess[str]:
        try:
            return subprocess.run(
                ["git", *arguments],
                cwd=repository,
                capture_output=True,
                text=True,
                check=False,
            )
        except OSError as exc:
            return subprocess.CompletedProcess(
                args=["git", *arguments],
                returncode=1,
                stdout="",
                stderr=str(exc),
            )
