from modules.analytics.indicator import Indicator
from modules.analytics.registry import IndicatorRegistry


def create_default_indicator_registry() -> IndicatorRegistry:
    registry = IndicatorRegistry()
    registry.register(
        Indicator(
            key="total_events",
            label="Total Events",
            calculator=lambda data: data.get("total_events", 0),
            unit="count",
        )
    )
    registry.register(
        Indicator(
            key="active_users",
            label="Active Users",
            calculator=lambda data: data.get("active_users", 0),
            unit="count",
        )
    )
    registry.register(
        Indicator(
            key="conversion_rate",
            label="Conversion Rate",
            calculator=lambda data: (
                data.get("conversions", 0) / data.get("visits", 1)
            )
            if data.get("visits", 0) > 0
            else data.get("conversion_rate", 0),
            unit="ratio",
        )
    )
    return registry
