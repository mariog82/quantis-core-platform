from dataclasses import dataclass, field
from typing import Literal
from uuid import uuid4

PermissionEffect = Literal["allow", "deny"]

@dataclass(frozen=True)
class PermissionId:
    value: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class Permission:
    id: PermissionId
    name: str
    resource: str
    action: str
    effect: PermissionEffect = "allow"

@dataclass(frozen=True)
class RoleId:
    value: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class Role:
    id: RoleId
    name: str
    description: str = ""
    permissions: list[Permission] = field(default_factory=list)

    def add_permission(self, permission: Permission) -> None:
        self.permissions.append(permission)

class RbacPolicy:
    def can(self, role: Role, resource: str, action: str) -> bool:
        decision = None
        for permission in role.permissions:
            if permission.resource == resource and permission.action == action:
                decision = permission.effect
        return decision == "allow"

class RoleRepository:
    def save(self, role: Role) -> Role:
        raise NotImplementedError

    def get(self, role_id: RoleId) -> Role | None:
        raise NotImplementedError

    def get_by_name(self, name: str) -> Role | None:
        raise NotImplementedError
