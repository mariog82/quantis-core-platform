from pathlib import Path


def test_m7_wp1_pr6_docs_exist():
    required = [
        "docs/m7/wp1/pr6-query-optimizer/README.md",
        "docs/m7/wp1/pr6-query-optimizer/ARCHITECTURE.md",
        "docs/m7/wp1/pr6-query-optimizer/TEST_PLAN.md",
        "docs/adr/ADR-091-m7-query-optimizer.md",
        "docs/rfc/RFC-034-m7-query-optimizer.md",
    ]

    for path in required:
        assert Path(path).exists(), path
