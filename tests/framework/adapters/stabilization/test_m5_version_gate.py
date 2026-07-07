from pathlib import Path


def test_m5_version_is_alpha_7_or_later():
    version = Path("VERSION").read_text(encoding="utf-8").strip()

    assert version.startswith("0.5.0-")
