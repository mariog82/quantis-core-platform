from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.identity.contracts import (
    IdentityToken,
    IdentityTokenValidationRequest,
    IdentityTokenValidationResponse,
    IdentityUser,
    IdentityUserLookupRequest,
    IdentityUserLookupResponse,
)


class IdentityProviderAdapter(Adapter):
    metadata = AdapterMetadata(
        name="identity-provider",
        adapter_type="identity_provider",
        version="0.5.0-beta.1",
        capabilities=["identity"],
        provider="quantis",
    )

    def validate_token(
        self,
        request: IdentityTokenValidationRequest,
    ) -> IdentityTokenValidationResponse:
        raise NotImplementedError

    def lookup_user(self, request: IdentityUserLookupRequest) -> IdentityUserLookupResponse:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}
        if operation == "validate_token":
            return AdapterResult.ok(self.validate_token(payload["request"]))
        if operation == "lookup_user":
            return AdapterResult.ok(self.lookup_user(payload["request"]))
        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryIdentityProviderAdapter(IdentityProviderAdapter):
    def __init__(self):
        super().__init__()
        self._users: dict[str, IdentityUser] = {}
        self._tokens: dict[str, str] = {}

    def register_user(
        self,
        user: IdentityUser,
        token: IdentityToken | None = None,
    ) -> IdentityUser:
        self._users[user.subject] = user
        if token:
            self._tokens[token.value] = user.subject
        return user

    def validate_token(
        self,
        request: IdentityTokenValidationRequest,
    ) -> IdentityTokenValidationResponse:
        subject = self._tokens.get(request.token.value)
        if subject is None:
            return IdentityTokenValidationResponse(False, error="INVALID_TOKEN")
        return IdentityTokenValidationResponse(True, self._users[subject])

    def lookup_user(self, request: IdentityUserLookupRequest) -> IdentityUserLookupResponse:
        user = self._users.get(request.subject or "")
        if not user and request.email:
            user = next(
                (candidate for candidate in self._users.values() if candidate.email == request.email),
                None,
            )
        return IdentityUserLookupResponse(
            user is not None,
            user,
            error=None if user else "USER_NOT_FOUND",
        )
