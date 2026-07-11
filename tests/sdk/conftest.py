"""Prevent tests/framework/adapters/sdk from shadowing application sdk."""

from tests.sdk._import_app_sdk import import_app_sdk


def pytest_configure() -> None:
    import_app_sdk()
