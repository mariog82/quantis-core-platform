from pathlib import Path


def test_m4_release_version_is_recorded():
    release_file = Path("docs/release/M4_BETA_FREEZE.md")
    assert release_file.exists()
    assert "0.4.0-beta.1" in release_file.read_text(encoding="utf-8")
