from pathlib import Path
def test_current_release_version():
    assert Path("VERSION").read_text(encoding="utf-8").strip()=="0.6.0-beta.1"
