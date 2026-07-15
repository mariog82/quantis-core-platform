from pathlib import Path


def test_current_release_version_is_m7_wp1_beta_1():
    assert Path("VERSION").read_text(encoding="utf-8").strip() == "0.7.0-beta.1"
