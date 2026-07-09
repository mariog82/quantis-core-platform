from pathlib import Path
def test_version():
    assert Path("VERSION").read_text().strip()=="0.6.0-alpha.2"
