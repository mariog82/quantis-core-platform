from pathlib import Path


def test_m6_final_release_documents_exist():
    required = [
        "docs/release/M6_FINAL_RELEASE.md",
        "docs/release/M6_FINAL_CHECKLIST.md",
        "docs/release/M6_PUBLIC_API_BASELINE.md",
        "docs/release/M6_MIGRATION_NOTES.md",
        "docs/adr/ADR-085-m6-final-release.md",
        "docs/rfc/RFC-028-m6-final-release.md",
    ]

    for path in required:
        assert Path(path).exists(), path
