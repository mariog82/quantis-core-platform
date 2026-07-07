from pathlib import Path


def test_version_file_is_present_and_semver_like():
    version = Path("VERSION").read_text(encoding="utf-8").strip()

    assert version
    assert version.count(".") >= 2
