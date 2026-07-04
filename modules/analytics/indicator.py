from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class IndicatorResult:
    key: str
    label: str
    value: float
    unit: str = "count"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Indicator:
    key: str
    label: str
    calculator: Callable[[dict[str, Any]], float]
    unit: str = "count"
    description: str = ""

    def calculate(self, data: dict[str, Any]) -> IndicatorResult:
        return IndicatorResult(
            key=self.key,
            label=self.label,
            value=float(self.calculator(data)),
            unit=self.unit,
        )
