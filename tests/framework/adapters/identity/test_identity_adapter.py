from framework.adapters.identity import (
    IdentityToken,
    IdentityTokenValidationRequest,
    IdentityUser,
    IdentityUserLookupRequest,
    InMemoryIdentityProviderAdapter,
)


def test_in_memory_identity_provider_validates_token():
    adapter = InMemoryIdentityProviderAdapter()
    user = IdentityUser(subject="user-1", email="user@example.com", roles=["admin"])
    token = IdentityToken(value="token-1")
    adapter.register_user(user, token)

    response = adapter.validate_token(IdentityTokenValidationRequest(token=token))

    assert response.valid is True
    assert response.user.subject == "user-1"
    assert response.user.has_role("admin") is True


def test_in_memory_identity_provider_rejects_invalid_token():
    adapter = InMemoryIdentityProviderAdapter()
    response = adapter.validate_token(
        IdentityTokenValidationRequest(token=IdentityToken(value="bad-token"))
    )
    assert response.valid is False
    assert response.error == "INVALID_TOKEN"


def test_in_memory_identity_provider_looks_up_user_by_email():
    adapter = InMemoryIdentityProviderAdapter()
    adapter.register_user(IdentityUser(subject="user-1", email="user@example.com"))

    response = adapter.lookup_user(IdentityUserLookupRequest(email="user@example.com"))

    assert response.found is True
    assert response.user.subject == "user-1"


def test_identity_adapter_execute_operations():
    adapter = InMemoryIdentityProviderAdapter()
    user = IdentityUser(subject="user-1", email="user@example.com")
    token = IdentityToken(value="token-1")
    adapter.register_user(user, token)

    validation = adapter.execute(
        "validate_token",
        {"request": IdentityTokenValidationRequest(token=token)},
    )
    lookup = adapter.execute(
        "lookup_user",
        {"request": IdentityUserLookupRequest(subject="user-1")},
    )

    assert validation.success is True
    assert validation.data.valid is True
    assert lookup.success is True
    assert lookup.data.found is True
