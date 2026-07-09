from pathlib import Path


def test_m5_2_version_is_rc_1():
    assert Path("VERSION").read_text(encoding="utf-8").strip() == "0.5.1-rc.1"
