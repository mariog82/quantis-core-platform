from pathlib import Path


def test_m6_wp1_pr7_docs_exist():
    assert Path("docs/m6/wp1/pr7-redis-streams/README.md").exists()
    assert Path("docs/m6/wp1/pr7-redis-streams/ARCHITECTURE.md").exists()
    assert Path("docs/adr/ADR-069-redis-streams-adapter.md").exists()
    assert Path("docs/rfc/RFC-012-redis-streams-api.md").exists()
