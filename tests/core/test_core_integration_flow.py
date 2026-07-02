from core.audit import AuditActor, AuditService
from core.configuration import ConfigurationService
from core.eventbus import EventBusService
from core.identity import IdentityService
from core.rbac import RbacService, RoleId
from core.tenant import TenantService


class MemoryIdentityRepository:
    def __init__(self):
        self.items = {}

    def save(self, identity):
        self.items[identity.id.value] = identity
        return identity

    def get(self, identity_id):
        return self.items.get(identity_id.value)

    def get_by_email(self, email):
        return next((i for i in self.items.values() if i.email == email), None)


class MemoryTenantRepository:
    def __init__(self):
        self.items = {}

    def save(self, tenant):
        self.items[tenant.id.value] = tenant
        return tenant

    def get(self, tenant_id):
        return self.items.get(tenant_id.value)

    def get_by_slug(self, slug):
        return next((t for t in self.items.values() if t.slug == slug), None)


class MemoryRoleRepository:
    def __init__(self):
        self.items = {}

    def save(self, role):
        self.items[role.id.value] = role
        return role

    def get(self, role_id):
        return self.items.get(role_id.value)

    def get_by_name(self, name):
        return next((r for r in self.items.values() if r.name == name), None)


class MemoryAuditRepository:
    def __init__(self):
        self.items = []

    def append(self, event):
        self.items.append(event)
        return event

    def list_by_tenant(self, tenant_id, limit=100):
        return [e for e in self.items if e.actor.tenant_id == tenant_id][:limit]


def test_core_foundation_integration_flow():
    identity_service = IdentityService(MemoryIdentityRepository())
    tenant_service = TenantService(MemoryTenantRepository())
    rbac_service = RbacService(MemoryRoleRepository())
    audit_service = AuditService(MemoryAuditRepository())
    config_service = ConfigurationService()
    eventbus = EventBusService()

    events = []
    eventbus.on("*", events.append)

    identity = identity_service.create_identity("admin@example.com", "Admin")
    tenant = tenant_service.create_tenant("Tenant Demo")
    role = rbac_service.create_role("owner")
    role = rbac_service.add_permission(RoleId(role.id.value), "tenant", "read")

    config_service.set("feature.core", True, scope="tenant", tenant_id=tenant.id.value)
    eventbus.emit("tenant.created", tenant.id.value, tenant_id=tenant.id.value)
    audit = audit_service.record(
        AuditActor(identity_id=identity.id.value, tenant_id=tenant.id.value),
        action="tenant.created",
        resource=f"tenant:{tenant.id.value}",
    )

    assert identity.email == "admin@example.com"
    assert tenant.slug == "tenant-demo"
    assert rbac_service.can(role, "tenant", "read") is True
    assert config_service.get("feature.core", tenant_id=tenant.id.value) is True
    assert len(events) == 1
    assert audit.outcome == "success"
