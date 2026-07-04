from modules.analytics import AnalyticsModule
from modules.dashboard import DashboardModule
from modules.notification import NotificationModule
from modules.reporting import ReportingModule


def test_default_module_manifests():
    modules = [
        AnalyticsModule(),
        ReportingModule(),
        DashboardModule(),
        NotificationModule(),
    ]

    names = [module.manifest.name for module in modules]

    assert names == ["analytics", "reporting", "dashboard", "notification"]
    assert "kpi" in AnalyticsModule.manifest.capabilities
    assert "export" in ReportingModule.manifest.capabilities
    assert "widgets" in DashboardModule.manifest.capabilities
    assert "alerts" in NotificationModule.manifest.capabilities
