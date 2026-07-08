from framework.adapters.identity import (
    IdentityToken,
    IdentityTokenValidationRequest,
    IdentityUser,
    IdentityUserLookupRequest,
    InMemoryIdentityProviderAdapter,
)
from framework.adapters.identity.runtime import IdentityProviderRuntime


def test_identity_provider_runtime_validates_and_looks_up_user():
    adapter = InMemoryIdentityProviderAdapter()
    user = IdentityUser(subject="user-1", email="user@example.com")
    token = IdentityToken(value="token-1")
    adapter.register_user(user, token)

    runtime = IdentityProviderRuntime(adapter)

    validation = runtime.validate_token(IdentityTokenValidationRequest(token=token))
    lookup = runtime.lookup_user(IdentityUserLookupRequest(email="user@example.com"))

    assert validation.valid is True
    assert lookup.found is True
