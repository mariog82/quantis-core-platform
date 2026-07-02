import re
from core.tenant.contracts import Tenant, TenantId, TenantRepository

class TenantService:
    def __init__(self, repository: TenantRepository):
        self.repository = repository

    def create_tenant(self, name: str, slug: str | None = None) -> Tenant:
        normalized_slug = slug or self._slugify(name)
        tenant = Tenant(id=TenantId(), name=name.strip(), slug=normalized_slug)
        return self.repository.save(tenant)

    def activate_tenant(self, tenant_id: TenantId) -> Tenant:
        tenant = self.repository.get(tenant_id)
        if tenant is None:
            raise ValueError("TENANT_NOT_FOUND")
        tenant.activate()
        return self.repository.save(tenant)

    def _slugify(self, value: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
        return slug or "tenant"
