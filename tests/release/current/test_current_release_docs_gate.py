from pathlib import Path


def test_m6_wp2_docs_exist():
    assert Path("docs/m6/wp2/README.md").exists()
    assert Path("docs/m6/wp2/ARCHITECTURE.md").exists()
    assert Path("docs/adr/ADR-073-m6-wp2-enterprise-events.md").exists()
    assert Path("docs/rfc/RFC-016-m6-wp2-enterprise-events.md").exists()
