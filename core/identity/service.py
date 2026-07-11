from core.identity.contracts import Identity, IdentityId, IdentityRepository

class IdentityService:
    def __init__(self, repository: IdentityRepository):
        self.repository = repository

    def create_identity(self, email: str, display_name: str) -> Identity:
        identity = Identity(
            id=IdentityId(),
            email=email.strip().lower(),
            display_name=display_name.strip(),
        )
        return self.repository.save(identity)

    def activate_identity(self, identity_id: IdentityId) -> Identity:
        identity = self.repository.get(identity_id)
        if identity is None:
            raise ValueError("IDENTITY_NOT_FOUND")
        identity.activate()
        return self.repository.save(identity)
