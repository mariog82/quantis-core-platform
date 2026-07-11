from framework.contracts.module import BaseModule, ModuleManifest
from modules.analytics.defaults import create_default_indicator_registry
from modules.analytics.engine import AnalyticsEngine


class AnalyticsModule(BaseModule):
    manifest = ModuleManifest(
        name="analytics",
        version="0.3.0-beta.1",
        description="Reusable analytics module foundation.",
        capabilities=["analytics", "kpi", "metrics", "indicators"],
    )

    def __init__(self):
        self.initialized = False
        self.started = False
        self.engine = AnalyticsEngine(create_default_indicator_registry())

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

    def calculate(self, key: str, data: dict):
        return self.engine.calculate(key, data)

    def calculate_all(self, data: dict):
        return self.engine.calculate_all(data)
