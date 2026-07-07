from abc import abstractmethod

from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.auth.contracts import (
    AuthProviderType,
    AuthRequest,
    AuthResult,
    Principal,
    PrincipalClaim,
)


class AuthenticationAdapter(Adapter):
    metadata = AdapterMetadata(
        name="auth",
        adapter_type="authentication",
        version="0.5.0-alpha.4",
        description="Provider-neutral authentication adapter contract.",
        capabilities=["auth", "authentication", "identity"],
        provider="quantis",
    )

    @abstractmethod
    def authenticate(self, request: AuthRequest) -> AuthResult:
        raise NotImplementedError

    @abstractmethod
    def validate_token(self, token: str) -> AuthResult:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}

        if operation == "authenticate":
            request = payload.get("request")
            if not isinstance(request, AuthRequest):
                return AdapterResult.fail("INVALID_AUTH_REQUEST")
            return AdapterResult.ok(self.authenticate(request))

        if operation == "validate_token":
            token = payload.get("token")
            if not isinstance(token, str):
                return AdapterResult.fail("INVALID_TOKEN")
            return AdapterResult.ok(self.validate_token(token))

        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryAuthenticationAdapter(AuthenticationAdapter):
    metadata = AdapterMetadata(
        name="memory-auth",
        adapter_type="authentication",
        version="0.5.0-alpha.4",
        description="In-memory authentication adapter for tests.",
        capabilities=["auth", "authentication", "identity"],
        provider=AuthProviderType.MEMORY.value,
    )

    def __init__(self):
        super().__init__()
        self._users: dict[str, tuple[str, Principal]] = {}
        self._tokens: dict[str, Principal] = {}

    def register_user(
        self,
        username: str,
        password: str,
        subject: str | None = None,
        roles: list[str] | None = None,
    ) -> Principal:
        principal = Principal(
            subject=subject or username,
            claims=[PrincipalClaim(name="username", value=username)],
            roles=roles or [],
        )
        self._users[username] = (password, principal)
        self._tokens[f"token:{username}"] = principal
        return principal

    def authenticate(self, request: AuthRequest) -> AuthResult:
        if request.username is None or request.password is None:
            return AuthResult.failure("MISSING_CREDENTIALS")

        user = self._users.get(request.username)
        if user is None:
            return AuthResult.failure("USER_NOT_FOUND")

        password, principal = user
        if password != request.password:
            return AuthResult.failure("INVALID_CREDENTIALS")

        return AuthResult.success(principal)

    def validate_token(self, token: str) -> AuthResult:
        principal = self._tokens.get(token)
        if principal is None:
            return AuthResult.failure("INVALID_TOKEN")
        return AuthResult.success(principal)
