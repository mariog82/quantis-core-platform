from dataclasses import dataclass, field


@dataclass
class RequestContext:
    request_id: str | None = None
    tenant_id: str | None = None
    actor_id: str | None = None
    correlation_id: str | None = None
    locale: str = "it-IT"
    metadata: dict = field(default_factory=dict)
