from modules.analytics.indicator import IndicatorResult
from modules.analytics.registry import IndicatorRegistry


class AnalyticsEngine:
    def __init__(self, registry: IndicatorRegistry | None = None):
        self.registry = registry or IndicatorRegistry()

    def calculate(self, key: str, data: dict) -> IndicatorResult:
        return self.registry.get(key).calculate(data)

    def calculate_all(self, data: dict) -> list[IndicatorResult]:
        return [indicator.calculate(data) for indicator in self.registry.list_indicators()]
