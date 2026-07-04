from framework.contracts.module import BaseModule, ModuleManifest


class AnalyticsModule(BaseModule):
    manifest = ModuleManifest(
        name="analytics",
        version="0.3.0-alpha.1",
        description="Reusable analytics module foundation.",
        capabilities=["analytics", "kpi", "metrics"],
    )

    def __init__(self):
        self.initialized = False
        self.started = False

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
