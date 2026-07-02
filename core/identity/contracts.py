from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4

IdentityStatus = Literal["active", "disabled", "pending", "locked"]

@dataclass(frozen=True)
class IdentityId:
    value: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class Identity:
    id: IdentityId
    email: str
    display_name: str
    status: IdentityStatus = "pending"
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def activate(self) -> None:
        self.status = "active"

    def disable(self) -> None:
        self.status = "disabled"

    def lock(self) -> None:
        self.status = "locked"

@dataclass
class IdentityCredentials:
    identity_id: IdentityId
    password_hash: str
    algorithm: str = "argon2id"

class IdentityRepository:
    def save(self, identity: Identity) -> Identity:
        raise NotImplementedError

    def get(self, identity_id: IdentityId) -> Identity | None:
        raise NotImplementedError

    def get_by_email(self, email: str) -> Identity | None:
        raise NotImplementedError
