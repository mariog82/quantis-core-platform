from modules.analytics.indicator import Indicator


class IndicatorRegistry:
    def __init__(self):
        self._items: dict[str, Indicator] = {}

    def register(self, indicator: Indicator) -> Indicator:
        self._items[indicator.key] = indicator
        return indicator

    def get(self, key: str) -> Indicator:
        return self._items[key]

    def exists(self, key: str) -> bool:
        return key in self._items

    def list_indicators(self) -> list[Indicator]:
        return list(self._items.values())
