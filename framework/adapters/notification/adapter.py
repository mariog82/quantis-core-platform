from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.notification.contracts import NotificationProviderType, NotificationRequest, NotificationResponse, NotificationStatus


class NotificationAdapter(Adapter):
    metadata = AdapterMetadata(name="notification", adapter_type="notification", version="0.5.0-beta.1", capabilities=["notification"], provider="quantis")

    def send(self, request: NotificationRequest) -> NotificationResponse:
        raise NotImplementedError

    def list_sent(self) -> list[NotificationResponse]:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        if operation == "send":
            return AdapterResult.ok(self.send((payload or {})["request"]))
        if operation == "list_sent":
            return AdapterResult.ok(self.list_sent())
        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryNotificationAdapter(NotificationAdapter):
    def __init__(self):
        super().__init__()
        self._responses: list[NotificationResponse] = []

    def send(self, request: NotificationRequest) -> NotificationResponse:
        response = NotificationResponse(status=NotificationStatus.SENT if request.recipients else NotificationStatus.FAILED, provider=NotificationProviderType.MEMORY, error=None if request.recipients else "NO_RECIPIENTS")
        self._responses.append(response)
        return response

    def list_sent(self) -> list[NotificationResponse]:
        return [r for r in self._responses if r.delivered]
