"""SDK adapter tests package.

This package defines __all__ so that the M5 public package gate remains stable
even when pytest places this test package on the import path during collection.
"""

__all__ = ["test_sdk_adapter", "test_sdk_factory"]
