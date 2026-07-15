from pathlib import Path


def test_m7_wp1_pr9_docs_exist():
    for path in [
        "docs/m7/wp1/pr9-semantic-layer/README.md",
        "docs/m7/wp1/pr9-semantic-layer/ARCHITECTURE.md",
        "docs/m7/wp1/pr9-semantic-layer/TEST_PLAN.md",
        "docs/adr/ADR-094-m7-semantic-layer.md",
        "docs/rfc/RFC-037-m7-semantic-layer.md",
    ]:
        assert Path(path).exists(), path
