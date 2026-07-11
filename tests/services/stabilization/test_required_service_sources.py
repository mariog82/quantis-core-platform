from pathlib import Path


REQUIRED_FILES = [
    "services/__init__.py",
    "services/base.py",
    "services/registry.py",
    "services/licensing/__init__.py",
    "services/licensing/service.py",
    "services/subscription/__init__.py",
    "services/subscription/service.py",
    "services/billing/__init__.py",
    "services/billing/service.py",
    "services/provisioning/__init__.py",
    "services/provisioning/service.py",
    "services/compliance/__init__.py",
    "services/compliance/service.py",
]


def test_required_service_sources_exist():
    missing = [path for path in REQUIRED_FILES if not Path(path).exists()]
    assert missing == []
