from modules.analytics import Indicator, IndicatorRegistry


def test_indicator_registry_registers_indicator():
    registry = IndicatorRegistry()
    indicator = Indicator(key="events", label="Events", calculator=lambda data: 10)

    registry.register(indicator)

    assert registry.exists("events")
    assert registry.get("events") == indicator
