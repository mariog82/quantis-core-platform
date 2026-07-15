from pathlib import Path

def test_m7_wp1_pr7_docs_exist():
    for path in [
        "docs/m7/wp1/pr7-graph-algorithms/README.md",
        "docs/m7/wp1/pr7-graph-algorithms/ARCHITECTURE.md",
        "docs/m7/wp1/pr7-graph-algorithms/TEST_PLAN.md",
        "docs/adr/ADR-092-m7-graph-algorithms.md",
        "docs/rfc/RFC-035-m7-graph-algorithms.md",
    ]:
        assert Path(path).exists(), path
