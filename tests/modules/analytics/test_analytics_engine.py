from modules.analytics import AnalyticsEngine
from modules.analytics.defaults import create_default_indicator_registry


def test_calculate_single_indicator():
    engine = AnalyticsEngine(create_default_indicator_registry())

    result = engine.calculate("total_events", {"total_events": 42})

    assert result.key == "total_events"
    assert result.value == 42


def test_calculate_all_indicators():
    engine = AnalyticsEngine(create_default_indicator_registry())

    results = engine.calculate_all(
        {
            "total_events": 100,
            "active_users": 25,
            "visits": 100,
            "conversions": 20,
        }
    )

    assert len(results) == 3
    assert {result.key for result in results} == {
        "total_events",
        "active_users",
        "conversion_rate",
    }
