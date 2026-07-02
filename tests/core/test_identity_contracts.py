from core.identity import IdentityId, IdentityService

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

def test_create_identity_normalizes_email():
    repo = MemoryIdentityRepository()
    service = IdentityService(repo)
    identity = service.create_identity(" USER@Example.COM ", "Mario Rossi")
    assert identity.email == "user@example.com"
    assert identity.status == "pending"

def test_activate_identity():
    repo = MemoryIdentityRepository()
    service = IdentityService(repo)
    identity = service.create_identity("user@example.com", "Mario Rossi")
    activated = service.activate_identity(IdentityId(identity.id.value))
    assert activated.status == "active"
