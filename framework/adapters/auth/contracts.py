from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from uuid import uuid4


class AuthProviderType(str, Enum):
    JWT = "jwt"
    OAUTH2 = "oauth2"
    OPENID_CONNECT = "openid_connect"
    LDAP = "ldap"
    SAML = "saml"
    MEMORY = "memory"


@dataclass(frozen=True)
class PrincipalClaim:
    name: str
    value: Any


@dataclass
class Principal:
    subject: str
    claims: list[PrincipalClaim] = field(default_factory=list)
    roles: list[str] = field(default_factory=list)

    def claim(self, name: str) -> Any:
        for claim in self.claims:
            if claim.name == name:
                return claim.value
        return None

    def has_role(self, role: str) -> bool:
        return role in self.roles


@dataclass
class AuthRequest:
    username: str | None = None
    password: str | None = None
    token: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class AuthSession:
    session_id: str = field(default_factory=lambda: str(uuid4()))
    principal: Principal | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class AuthResult:
    authenticated: bool
    principal: Principal | None = None
    session: AuthSession | None = None
    error: str | None = None

    @classmethod
    def success(cls, principal: Principal) -> "AuthResult":
        return cls(
            authenticated=True,
            principal=principal,
            session=AuthSession(principal=principal),
        )

    @classmethod
    def failure(cls, error: str) -> "AuthResult":
        return cls(authenticated=False, error=error)
