from pathlib import Path


def test_m6_wp4_pr8_docs_exist():
    assert Path(
        "docs/m6/wp4/pr8-workflow-monitoring/README.md"
    ).exists()
    assert Path(
        "docs/m6/wp4/pr8-workflow-monitoring/ARCHITECTURE.md"
    ).exists()
    assert Path(
        "docs/adr/ADR-082-m6-wp4-workflow-monitoring.md"
    ).exists()
    assert Path(
        "docs/rfc/RFC-025-m6-workflow-monitoring.md"
    ).exists()
