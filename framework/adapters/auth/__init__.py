from framework.adapters.auth.adapter import AuthenticationAdapter, InMemoryAuthenticationAdapter
from framework.adapters.auth.contracts import (
    AuthProviderType,
    AuthRequest,
    AuthResult,
    AuthSession,
    Principal,
    PrincipalClaim,
)

__all__ = [
    "AuthProviderType",
    "AuthRequest",
    "AuthResult",
    "AuthSession",
    "AuthenticationAdapter",
    "InMemoryAuthenticationAdapter",
    "Principal",
    "PrincipalClaim",
]
