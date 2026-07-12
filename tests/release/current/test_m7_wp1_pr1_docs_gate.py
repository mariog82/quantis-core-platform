from pathlib import Path

def test_m7_wp1_pr1_docs_exist():
    required = [
        "docs/m7/wp1/pr1-graph-core/README.md",
        "docs/m7/wp1/pr1-graph-core/ARCHITECTURE.md",
        "docs/m7/wp1/pr1-graph-core/TEST_PLAN.md",
        "docs/adr/ADR-086-m7-knowledge-graph-core.md",
        "docs/rfc/RFC-029-m7-knowledge-graph-core.md",
    ]
    for path in required:
        assert Path(path).exists(), path
