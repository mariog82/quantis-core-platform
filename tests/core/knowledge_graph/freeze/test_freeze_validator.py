from pathlib import Path
import subprocess

from core.knowledge_graph import KnowledgeGraphFreezeValidator


def initialize_repository(root: Path) -> None:
    subprocess.run(
        ["git", "init"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Quantis Test"],
        cwd=root,
        check=True,
    )
    subprocess.run(
        [
            "git",
            "config",
            "user.email",
            "quantis-test@example.invalid",
        ],
        cwd=root,
        check=True,
    )


def commit_repository(root: Path) -> None:
    subprocess.run(
        ["git", "add", "."],
        cwd=root,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "test fixture"],
        cwd=root,
        check=True,
        capture_output=True,
    )


def test_freeze_validator_passes_on_complete_fixture(
    tmp_path: Path,
):
    initialize_repository(tmp_path)

    required = (
        "core/knowledge_graph/graph.py",
        "core/knowledge_graph/semantic_layer.py",
    )

    for relative_path in required:
        path = tmp_path / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# valid\n", encoding="utf-8")

    (tmp_path / "VERSION").write_text(
        "0.7.0-beta.1\n",
        encoding="utf-8",
    )

    commit_repository(tmp_path)

    report = KnowledgeGraphFreezeValidator(
        required,
    ).validate(tmp_path)

    assert report.passed is True
    assert report.version == "0.7.0-beta.1"


def test_freeze_validator_detects_missing_artifact(
    tmp_path: Path,
):
    initialize_repository(tmp_path)

    (tmp_path / "VERSION").write_text(
        "0.7.0-beta.1\n",
        encoding="utf-8",
    )

    commit_repository(tmp_path)

    report = KnowledgeGraphFreezeValidator(
        ("core/knowledge_graph/missing.py",),
    ).validate(tmp_path)

    assert report.passed is False
    assert any(
        issue.code == "MISSING_REQUIRED_PATH"
        for issue in report.issues
    )
