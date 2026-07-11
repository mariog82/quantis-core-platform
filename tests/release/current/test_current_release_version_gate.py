from pathlib import Path


def test_current_release_version_is_m6_rc_1():
    assert (
        Path("VERSION").read_text(encoding="utf-8").strip()
        == "0.6.0-rc.1"
    )
