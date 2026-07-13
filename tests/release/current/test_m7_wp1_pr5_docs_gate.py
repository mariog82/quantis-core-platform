from pathlib import Path

def test_m7_wp1_pr5_docs_exist():
    for path in ["docs/m7/wp1/pr5-graph-query-engine/README.md","docs/m7/wp1/pr5-graph-query-engine/ARCHITECTURE.md","docs/m7/wp1/pr5-graph-query-engine/TEST_PLAN.md","docs/adr/ADR-090-m7-graph-query-engine.md","docs/rfc/RFC-033-m7-graph-query-engine.md"]:
        assert Path(path).exists(), path
