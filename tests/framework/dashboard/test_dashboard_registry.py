from framework.dashboard import Dashboard, DashboardId, DashboardRegistry


def test_register_and_get_dashboard():
    registry = DashboardRegistry()
    dashboard = Dashboard(id=DashboardId(), name="admin", title="Admin Dashboard", role="admin")

    registry.register(dashboard)

    assert registry.exists("admin")
    assert registry.get("admin") == dashboard


def test_find_by_role():
    registry = DashboardRegistry()
    registry.register(Dashboard(id=DashboardId(), name="admin", title="Admin", role="admin"))
    registry.register(Dashboard(id=DashboardId(), name="user", title="User", role="user"))

    assert len(registry.find_by_role("admin")) == 1
