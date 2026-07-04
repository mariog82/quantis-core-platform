from framework.dashboard.exceptions import DashboardNotFound
from framework.dashboard.models import Dashboard


class DashboardRegistry:
    def __init__(self):
        self._dashboards: dict[str, Dashboard] = {}

    def register(self, dashboard: Dashboard) -> Dashboard:
        self._dashboards[dashboard.name] = dashboard
        return dashboard

    def get(self, name: str) -> Dashboard:
        if name not in self._dashboards:
            raise DashboardNotFound(name)
        return self._dashboards[name]

    def exists(self, name: str) -> bool:
        return name in self._dashboards

    def list_dashboards(self) -> list[Dashboard]:
        return list(self._dashboards.values())

    def find_by_role(self, role: str) -> list[Dashboard]:
        return [dashboard for dashboard in self._dashboards.values() if dashboard.role == role]
