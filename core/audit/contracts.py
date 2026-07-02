from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4

AuditOutcome = Literal["success", "failure", "denied", "error"]

@dataclass(frozen=True)
class AuditEventId:
    value: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class AuditActor:
    identity_id: str
    tenant_id: str | None = None
    display_name: str | None = None

@dataclass
class AuditEvent:
    id: AuditEventId
    actor: AuditActor
    action: str
    resource: str
    outcome: AuditOutcome = "success"
    metadata: dict = field(default_factory=dict)
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class AuditRepository:
    def append(self, event: AuditEvent) -> AuditEvent:
        raise NotImplementedError

    def list_by_tenant(self, tenant_id: str, limit: int = 100) -> list[AuditEvent]:
        raise NotImplementedError
