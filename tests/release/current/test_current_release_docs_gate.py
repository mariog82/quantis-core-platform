from pathlib import Path


def test_m6_wp4_pr4_docs_exist():
    assert Path(
        "docs/m6/wp4/pr4-human-tasks/README.md"
    ).exists()
    assert Path(
        "docs/m6/wp4/pr4-human-tasks/ARCHITECTURE.md"
    ).exists()
    assert Path(
        "docs/adr/ADR-078-m6-wp4-human-tasks.md"
    ).exists()
    assert Path(
        "docs/rfc/RFC-021-m6-human-tasks.md"
    ).exists()
