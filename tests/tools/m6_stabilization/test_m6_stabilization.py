from pathlib import Path

from tools.m6_stabilization import run_m6_stabilization_checks


def _create_required_files(root: Path) -> None:
    (root / "VERSION").write_text("0.6.0\n", encoding="utf-8")

    required = [
        "docs/release/M6_FINAL_RELEASE.md",
        "docs/release/M6_FINAL_CHECKLIST.md",
        "docs/release/M6_PUBLIC_API_BASELINE.md",
        "docs/release/M6_MIGRATION_NOTES.md",
        "docs/adr/ADR-085-m6-final-release.md",
        "docs/rfc/RFC-028-m6-final-release.md",
        "core/workflow2/__init__.py",
        "core/event/__init__.py",
        "sdk/workflow/__init__.py",
    ]

    for relative in required:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# test\n", encoding="utf-8")


def test_m6_stabilization_passes_for_complete_repository(tmp_path: Path):
    _create_required_files(tmp_path)

    report = run_m6_stabilization_checks(tmp_path)

    assert report.passed is True


def test_m6_stabilization_detects_wrong_version(tmp_path: Path):
    _create_required_files(tmp_path)
    (tmp_path / "VERSION").write_text(
        "0.6.0-rc.1\n",
        encoding="utf-8",
    )

    report = run_m6_stabilization_checks(tmp_path)

    assert any(
        issue.code == "INVALID_VERSION"
        for issue in report.issues
    )


def test_m6_stabilization_detects_real_conflict_markers(tmp_path: Path):
    _create_required_files(tmp_path)
    source = tmp_path / "core" / "sample.py"
    source.write_text(
        "<<<<<<< HEAD\n"
        "value = 1\n"
        "=======\n"
        "value = 2\n"
        ">>>>>>> develop\n",
        encoding="utf-8",
    )

    report = run_m6_stabilization_checks(tmp_path)

    assert any(
        issue.code == "CONFLICT_MARKER"
        for issue in report.issues
    )


def test_m6_stabilization_ignores_marker_text_inside_source(tmp_path: Path):
    _create_required_files(tmp_path)
    source = tmp_path / "core" / "sample.py"
    source.write_text(
        'MARKERS = ("<<<<<<<", "=======", ">>>>>>>")\n',
        encoding="utf-8",
    )

    report = run_m6_stabilization_checks(tmp_path)

    assert report.passed is True
