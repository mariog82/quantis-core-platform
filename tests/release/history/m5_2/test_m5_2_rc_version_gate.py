from pathlib import Path


def test_m5_2_rc_release_version_is_recorded():
    release_file = Path('docs/release/M5_2_RELEASE_CANDIDATE.md')
    assert release_file.exists()
    assert '0.5.1-rc.1' in release_file.read_text(encoding='utf-8')
