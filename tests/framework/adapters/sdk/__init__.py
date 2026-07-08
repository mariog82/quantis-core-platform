"""SDK adapter tests package.

This package intentionally has a distinct __all__ for test discovery gates.
It must not be imported as the application `sdk` package.
"""

__all__ = [
    "test_sdk_adapter",
    "test_sdk_factory",
]
