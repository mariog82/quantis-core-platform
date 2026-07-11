from pathlib import Path
def test_freeze_docs():
    assert Path("docs/release/M6_WP1_FREEZE.md").exists()
    assert Path("docs/m6/wp1/pr10-freeze/README.md").exists()
