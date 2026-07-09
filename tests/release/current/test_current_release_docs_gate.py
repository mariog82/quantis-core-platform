from pathlib import Path


def test_m6_wp1_docs_exist():
    assert Path("docs/m6/wp1/README.md").exists()
    assert Path("docs/m6/wp1/PR_PLAN.md").exists()
