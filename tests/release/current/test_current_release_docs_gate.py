from pathlib import Path


def test_m6_wp4_pr9_docs_exist():
    assert Path(
        "docs/m6/wp4/pr9-workflow-api-sdk/README.md"
    ).exists()
    assert Path(
        "docs/m6/wp4/pr9-workflow-api-sdk/ARCHITECTURE.md"
    ).exists()
    assert Path(
        "docs/adr/ADR-083-m6-wp4-workflow-api-sdk.md"
    ).exists()
    assert Path(
        "docs/rfc/RFC-026-m6-workflow-api-sdk.md"
    ).exists()
