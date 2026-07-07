from pathlib import Path


def test_m5_version_is_alpha_8():
    assert Path("VERSION").read_text(encoding="utf-8").strip() == "0.5.0-alpha.8"
