from pathlib import Path


def test_m6_wp1_pr9_docs_exist():
    assert Path(
        "docs/m6/wp1/pr9-kafka/README.md"
    ).exists()
    assert Path(
        "docs/m6/wp1/pr9-kafka/ARCHITECTURE.md"
    ).exists()
    assert Path(
        "docs/adr/ADR-071-kafka-adapter.md"
    ).exists()
    assert Path(
        "docs/rfc/RFC-014-kafka-api.md"
    ).exists()
