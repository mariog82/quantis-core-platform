from pathlib import Path


def test_m6_wp4_pr3_docs_exist():
    assert Path(
        "docs/m6/wp4/pr3-state-machine/README.md"
    ).exists()
    assert Path(
        "docs/m6/wp4/pr3-state-machine/ARCHITECTURE.md"
    ).exists()
    assert Path(
        "docs/adr/ADR-077-m6-wp4-state-machine.md"
    ).exists()
    assert Path(
        "docs/rfc/RFC-020-m6-workflow-state-machine.md"
    ).exists()
