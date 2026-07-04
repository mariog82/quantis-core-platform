from pathlib import Path


REQUIRED_FILES = [
    "modules/__init__.py",
    "modules/registry.py",
    "modules/analytics/__init__.py",
    "modules/analytics/module.py",
    "modules/reporting/__init__.py",
    "modules/reporting/module.py",
    "modules/dashboard/__init__.py",
    "modules/dashboard/module.py",
    "modules/notification/__init__.py",
    "modules/notification/module.py",
]


def test_required_module_sources_exist():
    missing = [path for path in REQUIRED_FILES if not Path(path).exists()]
    assert missing == []
