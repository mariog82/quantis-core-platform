from framework.adapters.notification.adapter import NotificationAdapter
from framework.adapters.notification.contracts import NotificationRequest, NotificationResponse


class NotificationRuntime:
    def __init__(self, adapter: NotificationAdapter):
        self.adapter = adapter

    def send(self, request: NotificationRequest) -> NotificationResponse:
        return self.adapter.send(request)

    def list_sent(self) -> list[NotificationResponse]:
        return self.adapter.list_sent()
