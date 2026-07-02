from core.audit.contracts import AuditActor, AuditEvent, AuditEventId, AuditRepository

class AuditService:
    def __init__(self, repository: AuditRepository):
        self.repository = repository

    def record(
        self,
        actor: AuditActor,
        action: str,
        resource: str,
        outcome: str = "success",
        metadata: dict | None = None,
    ) -> AuditEvent:
        event = AuditEvent(
            id=AuditEventId(),
            actor=actor,
            action=action,
            resource=resource,
            outcome=outcome,
            metadata=metadata or {},
        )
        return self.repository.append(event)
