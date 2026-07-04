from dataclasses import dataclass, field
from typing import Any, Callable


WidgetProvider = Callable[[dict[str, Any]], Any]


@dataclass
class DashboardWidgetDefinition:
    key: str
    title: str
    provider: WidgetProvider
    description: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def resolve(self, data: dict[str, Any]) -> Any:
        return self.provider(data)
