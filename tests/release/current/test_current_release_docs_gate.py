from pathlib import Path


def test_m6_wp4_pr1_docs_exist():
    assert Path("docs/m6/wp4/pr1-workflow-core/README.md").exists()
    assert Path("docs/m6/wp4/pr1-workflow-core/ARCHITECTURE.md").exists()
    assert Path("docs/adr/ADR-075-m6-wp4-workflow-core.md").exists()
    assert Path("docs/rfc/RFC-018-m6-workflow-core.md").exists()
