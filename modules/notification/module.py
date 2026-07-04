from framework.contracts.module import BaseModule, ModuleManifest
from modules.notification.message import NotificationMessage
from modules.notification.service import NotificationService


class NotificationModule(BaseModule):
    manifest = ModuleManifest(
        name="notification",
        version="0.3.0-alpha.5",
        description="Reusable notification module foundation.",
        capabilities=["notification", "email", "alerts", "messages"],
    )

    def __init__(self):
        self.initialized = False
        self.started = False
        self.service = NotificationService()

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

    def send(self, recipient: str, subject: str, body: str) -> bool:
        return self.service.send_default(
            NotificationMessage(
                recipient=recipient,
                subject=subject,
                body=body,
            )
        )
