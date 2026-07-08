from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class IdentityProviderType(str, Enum):
    MEMORY = "memory"


class IdentityUserStatus(str, Enum):
    ACTIVE = "active"


@dataclass(frozen=True)
class IdentityUser:
    subject: str
    email: str | None = None
    roles: list[str] = field(default_factory=list)
    groups: list[str] = field(default_factory=list)
    claims: dict[str, Any] = field(default_factory=dict)

    def has_role(self, role: str) -> bool:
        return role in self.roles

    def belongs_to(self, group: str) -> bool:
        return group in self.groups


@dataclass(frozen=True)
class IdentityToken:
    value: str


@dataclass(frozen=True)
class IdentityTokenValidationRequest:
    token: IdentityToken


@dataclass
class IdentityTokenValidationResponse:
    valid: bool
    user: IdentityUser | None = None
    provider: IdentityProviderType = IdentityProviderType.MEMORY
    error: str | None = None


@dataclass(frozen=True)
class IdentityUserLookupRequest:
    subject: str | None = None
    email: str | None = None


@dataclass
class IdentityUserLookupResponse:
    found: bool
    user: IdentityUser | None = None
    provider: IdentityProviderType = IdentityProviderType.MEMORY
    error: str | None = None
