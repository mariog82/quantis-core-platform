from pathlib import Path


REQUIRED_FILES = [
    "framework/runtime/__init__.py",
    "framework/di/__init__.py",
    "framework/persistence/__init__.py",
    "framework/api/__init__.py",
    "framework/plugins/__init__.py",
    "framework/workflow/__init__.py",
    "framework/dashboard/__init__.py",
    "framework/reporting/__init__.py",
    "docs/release/M2_BETA_FREEZE.md",
    "docs/release/M2_RELEASE_NOTES.md",
    "docs/release/M2_ACCEPTANCE_CHECKLIST.md",
    "docs/release/M2_PUBLIC_API_BASELINE.md",
]


def test_required_m2_files_exist():
    missing = [path for path in REQUIRED_FILES if not Path(path).exists()]
    assert missing == []
