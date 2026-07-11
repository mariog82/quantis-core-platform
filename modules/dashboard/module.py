from framework.contracts.module import BaseModule, ModuleManifest
from modules.dashboard.defaults import create_default_dashboard_catalog
from modules.dashboard.service import DashboardModuleService


class DashboardModule(BaseModule):
    manifest = ModuleManifest(
        name="dashboard",
        version="0.3.0-beta.1",
        description="Reusable dashboard module foundation.",
        capabilities=["dashboard", "widgets", "visualization"],
        dependencies=["analytics"],
    )

    def __init__(self):
        self.initialized = False
        self.started = False
        self.service = DashboardModuleService()
        for widget in create_default_dashboard_catalog().list_widgets():
            self.service.register_widget(widget)

    def initialize(self, context):
        self.context = context
        self.initialized = True

    def boot(self):
        pass

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

    def shutdown(self):
        self.started = False

    def build_dashboard(self, name: str, title: str, data: dict) -> dict:
        return self.service.build_dashboard(name, title, data)
