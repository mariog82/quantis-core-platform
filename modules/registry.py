from framework.runtime import RuntimeManager
from modules.analytics import AnalyticsModule
from modules.dashboard import DashboardModule
from modules.notification import NotificationModule
from modules.reporting import ReportingModule


DEFAULT_MODULES = [
    AnalyticsModule,
    ReportingModule,
    DashboardModule,
    NotificationModule,
]


def register_default_modules(manager: RuntimeManager) -> RuntimeManager:
    for module_cls in DEFAULT_MODULES:
        manager.register(module_cls())
    return manager
