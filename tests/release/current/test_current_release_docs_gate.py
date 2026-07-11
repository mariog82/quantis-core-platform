from pathlib import Path


def test_m6_wp4_pr7_docs_exist():
    assert Path("docs/m6/wp4/pr7-saga-engine/README.md").exists()
    assert Path("docs/m6/wp4/pr7-saga-engine/ARCHITECTURE.md").exists()
    assert Path("docs/adr/ADR-081-m6-wp4-saga-engine.md").exists()
    assert Path("docs/rfc/RFC-024-m6-saga-engine.md").exists()
