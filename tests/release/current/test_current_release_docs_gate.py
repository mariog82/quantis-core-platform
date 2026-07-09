from pathlib import Path


def test_current_release_doc_exists():
    release_file = Path("docs/release/M5_2_RELEASE_CANDIDATE.md")
    assert release_file.exists()
    assert "0.5.1-rc.1" in release_file.read_text(encoding="utf-8")


def test_current_release_checklist_exists():
    checklist = Path("docs/release/M5_2_RC_CHECKLIST.md")
    assert checklist.exists()
    assert "v0.5.1-rc.1" in checklist.read_text(encoding="utf-8")
