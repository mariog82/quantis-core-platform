from pathlib import Path


def test_m6_wp1_pr3_docs_exist():
    assert Path("docs/m6/wp1/pr3-subscriber/README.md").exists()
    assert Path("docs/m6/wp1/pr3-subscriber/ARCHITECTURE.md").exists()
    assert Path("docs/adr/ADR-065-subscriber-layer.md").exists()
    assert Path("docs/rfc/RFC-008-subscriber-api.md").exists()
