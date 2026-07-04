from framework.contracts.module import BaseModule, ModuleManifest


class NotificationModule(BaseModule):
    manifest = ModuleManifest(
        name="notification",
        version="0.3.0-alpha.1",
        description="Reusable notification module foundation.",
        capabilities=["notification", "email", "alerts"],
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
