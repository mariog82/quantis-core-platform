from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.auth.contracts import AuthRequest, AuthResult, Principal, PrincipalClaim


class AuthenticationAdapter(Adapter):
    metadata = AdapterMetadata(name="auth", adapter_type="authentication", version="0.5.0-beta.1", capabilities=["auth"], provider="quantis")

    def authenticate(self, request: AuthRequest) -> AuthResult:
        raise NotImplementedError

    def validate_token(self, token: str) -> AuthResult:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}
        if operation == "authenticate":
            return AdapterResult.ok(self.authenticate(payload["request"]))
        if operation == "validate_token":
            return AdapterResult.ok(self.validate_token(payload["token"]))
        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryAuthenticationAdapter(AuthenticationAdapter):
    def __init__(self):
        super().__init__()
        self._users: dict[str, tuple[str, Principal]] = {}
        self._tokens: dict[str, Principal] = {}

    def register_user(self, username: str, password: str, roles: list[str] | None = None) -> Principal:
        principal = Principal(subject=username, claims=[PrincipalClaim("username", username)], roles=roles or [])
        self._users[username] = (password, principal)
        self._tokens[f"token:{username}"] = principal
        return principal

    def authenticate(self, request: AuthRequest) -> AuthResult:
        user = self._users.get(request.username or "")
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
