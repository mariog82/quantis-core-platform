from pathlib import Path


def test_m5_1_version_is_alpha_5():
    assert Path("VERSION").read_text(encoding="utf-8").strip() == "0.5.1-alpha.5"
