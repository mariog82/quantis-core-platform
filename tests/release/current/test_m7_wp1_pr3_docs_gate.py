from pathlib import Path


def test_m7_wp1_pr3_docs_exist():
    required = [
        "docs/m7/wp1/pr3-relationship-engine/README.md",
        "docs/m7/wp1/pr3-relationship-engine/ARCHITECTURE.md",
        "docs/m7/wp1/pr3-relationship-engine/TEST_PLAN.md",
        "docs/adr/ADR-088-m7-relationship-engine.md",
        "docs/rfc/RFC-031-m7-relationship-engine.md",
    ]

    for path in required:
        assert Path(path).exists(), path
