from pathlib import Path


def test_m7_wp1_pr8_docs_exist():
    required = [
        "docs/m7/wp1/pr8-graph-analytics/README.md",
        "docs/m7/wp1/pr8-graph-analytics/ARCHITECTURE.md",
        "docs/m7/wp1/pr8-graph-analytics/TEST_PLAN.md",
        "docs/adr/ADR-093-m7-graph-analytics.md",
        "docs/rfc/RFC-036-m7-graph-analytics.md",
    ]

    for path in required:
        assert Path(path).exists(), path
