from core.audit import AuditActor, AuditService

class MemoryAuditRepository:
    def __init__(self):
        self.items = []

    def append(self, event):
        self.items.append(event)
        return event

    def list_by_tenant(self, tenant_id, limit=100):
        return [e for e in self.items if e.actor.tenant_id == tenant_id][:limit]

def test_record_audit_event():
    repo = MemoryAuditRepository()
    service = AuditService(repo)
    event = service.record(
        actor=AuditActor(identity_id="user-1", tenant_id="tenant-1"),
        action="tenant.read",
        resource="tenant:tenant-1",
        metadata={"ip": "127.0.0.1"},
    )
    assert event.outcome == "success"
    assert event.metadata["ip"] == "127.0.0.1"

def test_list_audit_by_tenant():
    repo = MemoryAuditRepository()
    service = AuditService(repo)
    service.record(AuditActor(identity_id="user-1", tenant_id="tenant-1"), "read", "x")
    assert len(repo.list_by_tenant("tenant-1")) == 1
