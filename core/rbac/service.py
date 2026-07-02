from core.rbac.contracts import Permission, PermissionId, RbacPolicy, Role, RoleId, RoleRepository

class RbacService:
    def __init__(self, repository: RoleRepository):
        self.repository = repository
        self.policy = RbacPolicy()

    def create_role(self, name: str, description: str = "") -> Role:
        role = Role(id=RoleId(), name=name.strip(), description=description.strip())
        return self.repository.save(role)

    def add_permission(self, role_id: RoleId, resource: str, action: str, effect: str = "allow") -> Role:
        role = self.repository.get(role_id)
        if role is None:
            raise ValueError("ROLE_NOT_FOUND")
        role.add_permission(
            Permission(
                id=PermissionId(),
                name=f"{resource}:{action}",
                resource=resource,
                action=action,
                effect=effect,
            )
        )
        return self.repository.save(role)

    def can(self, role: Role, resource: str, action: str) -> bool:
        return self.policy.can(role, resource, action)
