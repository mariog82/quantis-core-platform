from modules.analytics import AnalyticsModule
from modules.dashboard import DashboardModule


def test_analytics_results_feed_dashboard_module():
    analytics = AnalyticsModule()
    dashboard = DashboardModule()

    results = analytics.calculate_all(
        {
            "total_events": 50,
            "active_users": 10,
            "visits": 100,
            "conversions": 25,
        }
    )

    data = {result.key: result.value for result in results}
    rendered = dashboard.build_dashboard("analytics", "Analytics Dashboard", data)

    assert rendered["name"] == "analytics"
    assert rendered["widgets"]["total-events"].value == 50
    assert rendered["widgets"]["active-users"].value == 10
    assert rendered["widgets"]["conversion-rate"].value == 0.25
