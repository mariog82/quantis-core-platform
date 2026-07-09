from pathlib import Path


def test_current_release_version_is_m6_alpha_1():
    assert Path("VERSION").read_text(encoding="utf-8").strip() == "0.6.0-alpha.1"
