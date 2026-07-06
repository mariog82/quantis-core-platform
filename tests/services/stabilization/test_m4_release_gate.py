from pathlib import Path


def test_m4_release_documents_exist():
    required = [
        "docs/release/M4_BETA_FREEZE.md",
        "docs/release/M4_RELEASE_NOTES.md",
        "docs/release/M4_ACCEPTANCE_CHECKLIST.md",
        "docs/release/M4_PUBLIC_API_BASELINE.md",
        "docs/release/M4_FINAL_RELEASE_GATE.md",
    ]

    missing = [path for path in required if not Path(path).exists()]
    assert missing == []
