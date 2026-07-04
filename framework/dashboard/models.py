from dataclasses import dataclass, field
from typing import Any, Callable
from uuid import uuid4


@dataclass(frozen=True)
class DashboardId:
    value: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class DashboardContext:
    tenant_id: str | None = None
    actor_id: str | None = None
    role: str | None = None
    filters: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class WidgetData:
    value: Any = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class DashboardWidget:
    key: str
    title: str
    provider: Callable[[DashboardContext], WidgetData]
    description: str = ""
    size: str = "medium"

    def render(self, context: DashboardContext) -> WidgetData:
        return self.provider(context)


@dataclass
class DashboardLayout:
    columns: int = 12
    widgets: list[str] = field(default_factory=list)


@dataclass
class Dashboard:
    id: DashboardId
    name: str
    title: str
    role: str | None = None
    layout: DashboardLayout = field(default_factory=DashboardLayout)
    widgets: dict[str, DashboardWidget] = field(default_factory=dict)

    def add_widget(self, widget: DashboardWidget) -> None:
        self.widgets[widget.key] = widget
        if widget.key not in self.layout.widgets:
            self.layout.widgets.append(widget.key)
