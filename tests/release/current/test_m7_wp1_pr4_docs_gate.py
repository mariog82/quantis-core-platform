from pathlib import Path

def test_m7_wp1_pr4_docs_exist():
    for path in [
        "docs/m7/wp1/pr4-graph-repository/README.md",
        "docs/m7/wp1/pr4-graph-repository/ARCHITECTURE.md",
        "docs/m7/wp1/pr4-graph-repository/TEST_PLAN.md",
        "docs/adr/ADR-089-m7-graph-repository.md",
        "docs/rfc/RFC-032-m7-graph-repository.md",
    ]:
        assert Path(path).exists(), path
