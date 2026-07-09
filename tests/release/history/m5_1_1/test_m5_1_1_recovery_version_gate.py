from pathlib import Path


def test_m5_1_1_repository_recovery_version_is_recorded():
    release_file = Path("docs/release/M5_1_1_REPOSITORY_RECOVERY.md")
    assert release_file.exists()
    assert "0.5.1-alpha.7" in release_file.read_text(encoding="utf-8")
