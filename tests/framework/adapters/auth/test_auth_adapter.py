from framework.adapters.auth import AuthRequest, InMemoryAuthenticationAdapter


def test_in_memory_authentication_adapter_authenticates_user():
    adapter = InMemoryAuthenticationAdapter()
    adapter.register_user("mario", "secret", roles=["admin"])

    result = adapter.authenticate(AuthRequest(username="mario", password="secret"))

    assert result.authenticated is True
    assert result.principal.has_role("admin") is True


def test_in_memory_authentication_adapter_rejects_wrong_password():
    adapter = InMemoryAuthenticationAdapter()
    adapter.register_user("mario", "secret")

    result = adapter.authenticate(AuthRequest(username="mario", password="wrong"))

    assert result.authenticated is False
    assert result.error == "INVALID_CREDENTIALS"


def test_in_memory_authentication_adapter_validates_token():
    adapter = InMemoryAuthenticationAdapter()
    adapter.register_user("mario", "secret")

    result = adapter.validate_token("token:mario")

    assert result.authenticated is True
    assert result.principal.subject == "mario"


def test_auth_adapter_execute_authenticate_operation():
    adapter = InMemoryAuthenticationAdapter()
    adapter.register_user("mario", "secret")

    result = adapter.execute(
        "authenticate",
        {"request": AuthRequest(username="mario", password="secret")},
    )

    assert result.success is True
    assert result.data.authenticated is True
