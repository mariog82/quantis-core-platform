from typing import Any

from framework.api.context import RequestContext
from framework.api.errors import ApiError
from framework.api.response import ApiResult, ResponseBuilder


class BaseController:
    def __init__(self, context: RequestContext | None = None):
        self.context = context or RequestContext()

    def ok(self, data: Any = None, metadata: dict | None = None) -> ApiResult:
        return ResponseBuilder.ok(data, metadata=metadata)

    def fail(
        self,
        code: str,
        message: str,
        details: dict | None = None,
        metadata: dict | None = None,
    ) -> ApiResult:
        return ResponseBuilder.fail(code, message, details=details, metadata=metadata)

    def handle_error(self, error: Exception) -> ApiResult:
        if isinstance(error, ApiError):
            return self.fail(error.code, error.message, details=error.details)
        return self.fail("INTERNAL_ERROR", "Internal server error")
