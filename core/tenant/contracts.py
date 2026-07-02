from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4

TenantStatus = Literal["active", "suspended", "provisioning", "deleted"]

@dataclass(frozen=True)
class TenantId:
    value: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class Tenant:
    id: TenantId
    name: str
    slug: str
    status: TenantStatus = "provisioning"
    metadata: dict = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def activate(self) -> None:
        self.status = "active"

    def suspend(self) -> None:
        self.status = "suspended"

@dataclass
class TenantMembership:
    tenant_id: TenantId
    identity_id: str
    roles: list[str] = field(default_factory=list)

class TenantRepository:
    def save(self, tenant: Tenant) -> Tenant:
        raise NotImplementedError

    def get(self, tenant_id: TenantId) -> Tenant | None:
        raise NotImplementedError

    def get_by_slug(self, slug: str) -> Tenant | None:
        raise NotImplementedError
