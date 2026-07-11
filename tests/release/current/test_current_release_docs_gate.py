from pathlib import Path


def test_m6_wp1_pr6_docs_exist():
    assert Path("docs/m6/wp1/pr6-inmemory-event-bus/README.md").exists()
    assert Path("docs/adr/ADR-068-inmemory-event-bus.md").exists()
    assert Path("docs/rfc/RFC-011-event-bus-api.md").exists()
