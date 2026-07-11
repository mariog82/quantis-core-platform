from pathlib import Path


def test_m6_wp4_pr5_docs_exist():
    assert Path(
        "docs/m6/wp4/pr5-timers-scheduling/README.md"
    ).exists()
    assert Path(
        "docs/m6/wp4/pr5-timers-scheduling/ARCHITECTURE.md"
    ).exists()
    assert Path(
        "docs/adr/ADR-079-m6-wp4-timers-scheduling.md"
    ).exists()
    assert Path(
        "docs/rfc/RFC-022-m6-timers-scheduling.md"
    ).exists()
