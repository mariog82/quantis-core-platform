from pathlib import Path


def test_m6_wp1_pr8_docs_exist():
    assert Path(
        "docs/m6/wp1/pr8-rabbitmq/README.md"
    ).exists()
    assert Path(
        "docs/m6/wp1/pr8-rabbitmq/ARCHITECTURE.md"
    ).exists()
    assert Path(
        "docs/adr/ADR-070-rabbitmq-adapter.md"
    ).exists()
    assert Path(
        "docs/rfc/RFC-013-rabbitmq-api.md"
    ).exists()
