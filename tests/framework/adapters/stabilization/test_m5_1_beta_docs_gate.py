from pathlib import Path


def test_m5_1_beta_freeze_doc_exists():
    release_file = Path("docs/release/M5_1_BETA_FREEZE.md")

    assert release_file.exists()
    assert "0.5.1-beta.1" in release_file.read_text(encoding="utf-8")


def test_m5_1_beta_checklist_exists():
    checklist = Path("docs/release/M5_1_BETA_CHECKLIST.md")

    assert checklist.exists()
    assert "v0.5.1-beta.1" in checklist.read_text(encoding="utf-8")
