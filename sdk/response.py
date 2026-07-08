from dataclasses import dataclass
from typing import Any


@dataclass
class SDKResponse:
    success: bool
    data: Any = None
    error: str | None = None
    status_code: int | None = None

    @classmethod
    def ok(cls, data: Any = None, status_code: int | None = None) -> "SDKResponse":
        return cls(success=True, data=data, status_code=status_code)

    @classmethod
    def fail(cls, error: str, status_code: int | None = None) -> "SDKResponse":
        return cls(success=False, error=error, status_code=status_code)
