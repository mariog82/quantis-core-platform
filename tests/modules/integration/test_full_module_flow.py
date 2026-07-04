from modules.analytics import AnalyticsModule
from modules.dashboard import DashboardModule
from modules.notification import NotificationModule
from modules.reporting import ReportingModule


def test_full_module_flow_analytics_dashboard_reporting_notification():
    analytics = AnalyticsModule()
    reporting = ReportingModule()
    dashboard = DashboardModule()
    notification = NotificationModule()

    raw_data = {
        "total_events": 200,
        "active_users": 50,
        "visits": 400,
        "conversions": 100,
    }

    indicators = analytics.calculate_all(raw_data)
    indicator_data = {result.key: result.value for result in indicators}

    rendered_dashboard = dashboard.build_dashboard(
        "executive",
        "Executive Dashboard",
        indicator_data,
    )

    report_content = reporting.generate("summary", indicator_data)

    notification.send(
        recipient="owner@example.com",
        subject="Executive Summary",
        body=report_content.decode("utf-8"),
    )

    assert rendered_dashboard["widgets"]["total-events"].value == 200
    assert b"active_users: 50" in report_content or b"active_users: 50.0" in report_content
    assert notification.service.registry.get("memory").messages[0].subject == "Executive Summary"
