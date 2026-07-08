from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from uuid import uuid4


class AuthProviderType(str, Enum):
    MEMORY = "memory"
    JWT = "jwt"
    OAUTH2 = "oauth2"


@dataclass(frozen=True)
class PrincipalClaim:
    name: str
    value: Any


@dataclass
class Principal:
    subject: str
    claims: list[PrincipalClaim] = field(default_factory=list)
    roles: list[str] = field(default_factory=list)

    def has_role(self, role: str) -> bool:
        return role in self.roles


@dataclass
class AuthRequest:
    username: str | None = None
    password: str | None = None
    token: str | None = None


@dataclass
class AuthSession:
    session_id: str = field(default_factory=lambda: str(uuid4()))
    principal: Principal | None = None


@dataclass
class AuthResult:
    authenticated: bool
    principal: Principal | None = None
    session: AuthSession | None = None
    error: str | None = None

    @classmethod
    def success(cls, principal: Principal) -> "AuthResult":
        return cls(True, principal, AuthSession(principal=principal))

    @classmethod
    def failure(cls, error: str) -> "AuthResult":
        return cls(False, error=error)
