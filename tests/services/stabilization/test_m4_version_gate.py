from pathlib import Path


def test_m4_version_is_alpha_2():
    assert Path("VERSION").read_text(encoding="utf-8").strip() == "0.4.0-alpha.2"
