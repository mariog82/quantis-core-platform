from abc import abstractmethod

from framework.adapters import Adapter, AdapterMetadata, AdapterResult
from framework.adapters.notification.contracts import (
    NotificationProviderType,
    NotificationRequest,
    NotificationResponse,
    NotificationStatus,
)


class NotificationAdapter(Adapter):
    metadata = AdapterMetadata(
        name="notification",
        adapter_type="notification",
        version="0.5.0-alpha.8",
        description="Provider-neutral notification adapter contract.",
        capabilities=["notification", "email", "sms", "push", "chat"],
        provider="quantis",
    )

    @abstractmethod
    def send(self, request: NotificationRequest) -> NotificationResponse:
        raise NotImplementedError

    @abstractmethod
    def list_sent(self) -> list[NotificationResponse]:
        raise NotImplementedError

    def execute(self, operation: str, payload: dict | None = None) -> AdapterResult:
        payload = payload or {}

        if operation == "send":
            request = payload.get("request")
            if not isinstance(request, NotificationRequest):
                return AdapterResult.fail("INVALID_NOTIFICATION_REQUEST")
            return AdapterResult.ok(self.send(request))

        if operation == "list_sent":
            return AdapterResult.ok(self.list_sent())

        return AdapterResult.fail("UNSUPPORTED_OPERATION")


class InMemoryNotificationAdapter(NotificationAdapter):
    metadata = AdapterMetadata(
        name="memory-notification",
        adapter_type="notification",
        version="0.5.0-alpha.8",
        description="In-memory notification adapter for tests.",
        capabilities=["notification", "email", "sms", "push", "chat"],
        provider=NotificationProviderType.MEMORY.value,
    )

    def __init__(self):
        super().__init__()
        self._requests: list[NotificationRequest] = []
        self._responses: list[NotificationResponse] = []

    def send(self, request: NotificationRequest) -> NotificationResponse:
        if not request.recipients:
            response = NotificationResponse(
                status=NotificationStatus.FAILED,
                provider=NotificationProviderType.MEMORY,
                error="NO_RECIPIENTS",
            )
        else:
            response = NotificationResponse(
                status=NotificationStatus.SENT,
                provider=NotificationProviderType.MEMORY,
                metadata={
                    "recipient_count": len(request.recipients),
                    "channel": request.channel.value,
                    "priority": request.priority.value,
                },
            )

        self._requests.append(request)
        self._responses.append(response)
        return response

    def list_sent(self) -> list[NotificationResponse]:
        return [
            response
            for response in self._responses
            if response.status == NotificationStatus.SENT
        ]

    def list_requests(self) -> list[NotificationRequest]:
        return list(self._requests)
