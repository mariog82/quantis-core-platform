from pathlib import Path


def test_m5_1_version_is_alpha_6():
    assert Path("VERSION").read_text(encoding="utf-8").strip() == "0.5.1-alpha.6"
