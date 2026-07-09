from pathlib import Path


def test_m6_wp1_pr1_docs_exist():
    assert Path("docs/m6/wp1/pr1-event-core/README.md").exists()
    assert Path("docs/m6/wp1/pr1-event-core/ARCHITECTURE.md").exists()
    assert Path("docs/adr/ADR-063-m6-wp1-pr1-event-core.md").exists()
    assert Path("docs/rfc/RFC-006-m6-event-core.md").exists()
