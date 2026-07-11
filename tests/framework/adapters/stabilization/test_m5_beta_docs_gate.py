from pathlib import Path


def test_m5_beta_required_release_docs_exist():
    required = [
        "docs/release/M5_BETA_FREEZE.md",
        "docs/release/M5_RELEASE_NOTES.md",
        "docs/release/M5_ACCEPTANCE_CHECKLIST.md",
        "docs/release/M5_PUBLIC_API_BASELINE.md",
        "docs/release/M5_FINAL_RELEASE_GATE.md",
        "docs/release/M5_REGRESSION_MATRIX.md",
    ]

    missing = [path for path in required if not Path(path).exists()]
    assert missing == []
