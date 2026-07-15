from pathlib import Path

def test_m7_wp1_pr2_docs_exist():
    for path in [
        "docs/m7/wp1/pr2-entity-registry/README.md",
        "docs/m7/wp1/pr2-entity-registry/ARCHITECTURE.md",
        "docs/m7/wp1/pr2-entity-registry/TEST_PLAN.md",
        "docs/adr/ADR-087-m7-entity-registry.md",
        "docs/rfc/RFC-030-m7-entity-registry.md",
    ]:
        assert Path(path).exists(), path
