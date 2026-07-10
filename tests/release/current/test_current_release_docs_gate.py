from pathlib import Path


def test_m6_wp1_pr4_docs_exist():
    assert Path("docs/m6/wp1/pr4-dispatcher/README.md").exists()
    assert Path("docs/m6/wp1/pr4-dispatcher/ARCHITECTURE.md").exists()
    assert Path("docs/adr/ADR-066-dispatcher-layer.md").exists()
    assert Path("docs/rfc/RFC-009-dispatcher-api.md").exists()
