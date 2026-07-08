from framework.adapters.identity import IdentityUser


def test_identity_user_roles_and_groups():
    user = IdentityUser(
        subject="user-1",
        email="user@example.com",
        roles=["admin"],
        groups=["staff"],
    )
    assert user.has_role("admin") is True
    assert user.belongs_to("staff") is True
