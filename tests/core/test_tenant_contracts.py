from core.tenant import TenantId, TenantService

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

def test_create_tenant_generates_slug():
    repo = MemoryTenantRepository()
    service = TenantService(repo)
    tenant = service.create_tenant("Istituto Demo")
    assert tenant.slug == "istituto-demo"
    assert tenant.status == "provisioning"

def test_activate_tenant():
    repo = MemoryTenantRepository()
    service = TenantService(repo)
    tenant = service.create_tenant("Tenant Demo")
    activated = service.activate_tenant(TenantId(tenant.id.value))
    assert activated.status == "active"
