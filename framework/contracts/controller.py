from dataclasses import dataclass, field


@dataclass
class ApiResponse:
    success: bool
    data: dict | list | None = None
    error: dict | None = None
    metadata: dict = field(default_factory=dict)


class BaseController:
    def ok(self, data=None, metadata: dict | None = None) -> ApiResponse:
        return ApiResponse(success=True, data=data, metadata=metadata or {})

    def fail(self, code: str, message: str, metadata: dict | None = None) -> ApiResponse:
        return ApiResponse(
            success=False,
            error={"code": code, "message": message},
            metadata=metadata or {},
        )