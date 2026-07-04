from modules.analytics import AnalyticsModule
from modules.reporting import ReportingModule


def test_analytics_results_feed_reporting_module():
    analytics = AnalyticsModule()
    reporting = ReportingModule()

    analytics.initialize(context={})
    reporting.initialize(context={})
    analytics.start()
    reporting.start()

    results = analytics.calculate_all(
        {
            "total_events": 100,
            "active_users": 25,
            "visits": 100,
            "conversions": 20,
        }
    )

    data = {result.key: result.value for result in results}
    content = reporting.generate("summary", data)

    assert b"Summary Report" in content
    assert b"total_events: 100" in content or b"total_events: 100.0" in content
    assert b"active_users: 25" in content or b"active_users: 25.0" in content
