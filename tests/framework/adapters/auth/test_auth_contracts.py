from framework.adapters.auth import AuthResult, Principal, PrincipalClaim


def test_principal_claim_and_role_lookup():
    principal = Principal(
        subject="user-1",
        claims=[PrincipalClaim(name="email", value="user@example.com")],
        roles=["admin"],
    )

    assert principal.claim("email") == "user@example.com"
    assert principal.has_role("admin") is True


def test_auth_result_success_creates_session():
    principal = Principal(subject="user-1")

    result = AuthResult.success(principal)

    assert result.authenticated is True
    assert result.session.principal == principal
