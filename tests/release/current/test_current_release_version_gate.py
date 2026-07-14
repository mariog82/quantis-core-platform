from pathlib import Path


def test_current_release_version_is_m7_alpha_6():
    assert (
        Path("VERSION").read_text(encoding="utf-8").strip()
        == "0.7.0-alpha.6"
    )
