from dataclasses import dataclass, field

@dataclass
class ServiceContext:
    tenant_id: str | None = None
    actor_id: str | None = None
    correlation_id: str | None = None
    metadata: dict = field(default_factory=dict)

class BaseService:
    def __init__(self, context: ServiceContext | None = None):
        self.context = context or ServiceContext()
