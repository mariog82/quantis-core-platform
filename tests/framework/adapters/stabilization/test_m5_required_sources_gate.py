from pathlib import Path


REQUIRED_FILES = [
    "framework/adapters/__init__.py",
    "framework/adapters/adapter.py",
    "framework/adapters/context.py",
    "framework/adapters/exceptions.py",
    "framework/adapters/factory.py",
    "framework/adapters/metadata.py",
    "framework/adapters/registry.py",
    "framework/adapters/result.py",
    "framework/adapters/runtime.py",
    "framework/adapters/ai/__init__.py",
    "framework/adapters/auth/__init__.py",
    "framework/adapters/database/__init__.py",
    "framework/adapters/http/__init__.py",
    "framework/adapters/identity/__init__.py",
    "framework/adapters/messaging/__init__.py",
    "framework/adapters/notification/__init__.py",
    "framework/adapters/payment/__init__.py",
    "framework/adapters/sdk/__init__.py",
    "framework/adapters/storage/__init__.py",
    "sdk/__init__.py",
    "sdk/client.py",
    "sdk/config.py",
    "sdk/response.py",
    "sdk/generator/__init__.py",
]


def test_m5_required_sources_exist():
    missing = [path for path in REQUIRED_FILES if not Path(path).exists()]
    assert missing == []
