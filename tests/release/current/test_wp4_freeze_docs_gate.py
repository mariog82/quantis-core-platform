from pathlib import Path


def test_wp4_freeze_documents_exist():
    required = [
        "docs/m6/wp4/pr10-freeze/README.md",
        "docs/m6/wp4/pr10-freeze/CHECKLIST.md",
        "docs/m6/wp4/pr10-freeze/ARCHITECTURE.md",
        "docs/m6/wp4/pr10-freeze/TEST_PLAN.md",
        "docs/release/M6_WP4_FREEZE.md",
        "docs/release/M6_WP4_PUBLIC_API_FREEZE.md",
        "docs/adr/ADR-084-m6-wp4-freeze.md",
        "docs/rfc/RFC-027-m6-wp4-freeze.md",
    ]

    for path in required:
        assert Path(path).exists(), path
