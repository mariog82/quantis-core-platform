from dataclasses import dataclass

@dataclass
class PlatformError(Exception):
    code: str
    message: str
    details: dict | None = None

class EntityNotFoundError(PlatformError):
    pass

class ValidationError(PlatformError):
    pass
