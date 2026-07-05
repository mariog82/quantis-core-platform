from pathlib import Path


def test_m3_version_is_beta_1():
    assert Path("VERSION").read_text(encoding="utf-8").strip() == "0.4.0-alpha.2"


def test_m3_release_documents_exist():
    required = [
        "docs/release/M3_BETA_FREEZE.md",
        "docs/release/M3_RELEASE_NOTES.md",
        "docs/release/M3_ACCEPTANCE_CHECKLIST.md",
        "docs/release/M3_PUBLIC_API_BASELINE.md",
        "docs/release/M3_FINAL_RELEASE_GATE.md",
    ]

    missing = [path for path in required if not Path(path).exists()]

    assert missing == []
