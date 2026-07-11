from pathlib import Path


def test_m6_wp4_pr2_docs_exist():
    assert Path(
        "docs/m6/wp4/pr2-workflow-runtime/README.md"
    ).exists()
    assert Path(
        "docs/m6/wp4/pr2-workflow-runtime/ARCHITECTURE.md"
    ).exists()
    assert Path(
        "docs/adr/ADR-076-m6-wp4-workflow-runtime.md"
    ).exists()
    assert Path(
        "docs/rfc/RFC-019-m6-workflow-runtime.md"
    ).exists()
