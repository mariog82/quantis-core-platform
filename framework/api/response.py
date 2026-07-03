from dataclasses import dataclass, field
from typing import Any


@dataclass
class ErrorResponse:
    code: str
    message: str
    details: dict = field(default_factory=dict)


@dataclass
class SuccessResponse:
    data: Any = None
    metadata: dict = field(default_factory=dict)


@dataclass
class ApiResult:
    success: bool
    data: Any = None
    error: ErrorResponse | None = None
    metadata: dict = field(default_factory=dict)


class ResponseBuilder:
    @staticmethod
    def ok(data: Any = None, metadata: dict | None = None) -> ApiResult:
        return ApiResult(success=True, data=data, metadata=metadata or {})

    @staticmethod
    def fail(
        code: str,
        message: str,
        details: dict | None = None,
        metadata: dict | None = None,
    ) -> ApiResult:
        return ApiResult(
            success=False,
            error=ErrorResponse(code=code, message=message, details=details or {}),
            metadata=metadata or {},
        )
