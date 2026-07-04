from modules.dashboard import DashboardWidgetDefinition


def test_dashboard_widget_resolves_value():
    widget = DashboardWidgetDefinition(
        key="total",
        title="Total",
        provider=lambda data: data["total"],
    )

    assert widget.resolve({"total": 5}) == 5
