from dataclasses import dataclass, field
from typing import Any


@dataclass
class ServiceResult:
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


class EnterpriseService:
    name: str = "enterprise-service"

    def health(self) -> ServiceResult:
        return ServiceResult(success=True, data={"service": self.name})
