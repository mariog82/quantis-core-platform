class ApiError(Exception):
    def __init__(self, code: str, message: str, details: dict | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details or {}


class ApiValidationError(ApiError):
    def __init__(self, message: str = "Validation error", details: dict | None = None):
        super().__init__("API_VALIDATION_ERROR", message, details)


class UnauthorizedError(ApiError):
    def __init__(self, message: str = "Unauthorized", details: dict | None = None):
        super().__init__("UNAUTHORIZED", message, details)


class NotFoundError(ApiError):
    def __init__(self, message: str = "Resource not found", details: dict | None = None):
        super().__init__("NOT_FOUND", message, details)
