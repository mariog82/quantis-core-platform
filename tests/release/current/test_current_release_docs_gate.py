from pathlib import Path


def test_m6_wp3_docs_exist():
    assert Path("docs/m6/wp3/README.md").exists()
    assert Path("docs/m6/wp3/ARCHITECTURE.md").exists()
    assert Path("docs/adr/ADR-074-m6-wp3-cqrs-projections.md").exists()
    assert Path("docs/rfc/RFC-017-m6-wp3-cqrs-projections.md").exists()
