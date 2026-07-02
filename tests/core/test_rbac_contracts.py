from core.rbac import RbacService, RoleId

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

def test_create_role():
    repo = MemoryRoleRepository()
    service = RbacService(repo)
    role = service.create_role("admin", "Administrator")
    assert role.name == "admin"

def test_permission_allows_action():
    repo = MemoryRoleRepository()
    service = RbacService(repo)
    role = service.create_role("admin")
    role = service.add_permission(RoleId(role.id.value), "tenant", "read")
    assert service.can(role, "tenant", "read") is True
    assert service.can(role, "tenant", "delete") is False
