from abc import abstractmethod

from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.identity.contracts import (
    IdentityProviderType,
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
        description="Provider-neutral identity provider adapter contract.",
        capabilities=["identity", "token-validation", "user-lookup", "roles", "groups"],
        provider="quantis",
    )

    @abstractmethod
    def validate_token(self, request: IdentityTokenValidationRequest) -> IdentityTokenValidationResponse:
        raise NotImplementedError

    @abstractmethod
    def lookup_user(self, request: IdentityUserLookupRequest) -> IdentityUserLookupResponse:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}

        if operation == "validate_token":
            request = payload.get("request")
            if not isinstance(request, IdentityTokenValidationRequest):
                return AdapterResult.fail("INVALID_IDENTITY_TOKEN_VALIDATION_REQUEST")
            return AdapterResult.ok(self.validate_token(request))

        if operation == "lookup_user":
            request = payload.get("request")
            if not isinstance(request, IdentityUserLookupRequest):
                return AdapterResult.fail("INVALID_IDENTITY_USER_LOOKUP_REQUEST")
            return AdapterResult.ok(self.lookup_user(request))

        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryIdentityProviderAdapter(IdentityProviderAdapter):
    metadata = AdapterMetadata(
        name="memory-identity-provider",
        adapter_type="identity_provider",
        version="0.5.0-beta.1",
        description="In-memory identity provider adapter for tests.",
        capabilities=["identity", "token-validation", "user-lookup", "roles", "groups"],
        provider=IdentityProviderType.MEMORY.value,
    )

    def __init__(self):
        super().__init__()
        self._users_by_subject: dict[str, IdentityUser] = {}
        self._subjects_by_email: dict[str, str] = {}
        self._tokens: dict[str, str] = {}

    def register_user(self, user: IdentityUser, token: IdentityToken | None = None) -> IdentityUser:
        self._users_by_subject[user.subject] = user
        if user.email is not None:
            self._subjects_by_email[user.email] = user.subject
        if token is not None:
            self._tokens[token.value] = user.subject
        return user

    def issue_token(self, subject: str, token_value: str) -> IdentityToken:
        if subject not in self._users_by_subject:
            raise KeyError(subject)
        token = IdentityToken(value=token_value)
        self._tokens[token.value] = subject
        return token

    def validate_token(self, request: IdentityTokenValidationRequest) -> IdentityTokenValidationResponse:
        subject = self._tokens.get(request.token.value)
        if subject is None:
            return IdentityTokenValidationResponse(valid=False, error="INVALID_TOKEN")
        user = self._users_by_subject.get(subject)
        if user is None:
            return IdentityTokenValidationResponse(valid=False, error="USER_NOT_FOUND")
        return IdentityTokenValidationResponse(valid=True, user=user)

    def lookup_user(self, request: IdentityUserLookupRequest) -> IdentityUserLookupResponse:
        user = None
        if request.subject is not None:
            user = self._users_by_subject.get(request.subject)
        if user is None and request.email is not None:
            subject = self._subjects_by_email.get(request.email)
            if subject is not None:
                user = self._users_by_subject.get(subject)
        if user is None:
            return IdentityUserLookupResponse(found=False, error="USER_NOT_FOUND")
        return IdentityUserLookupResponse(found=True, user=user)
