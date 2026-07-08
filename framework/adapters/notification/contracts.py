from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4


class NotificationProviderType(str, Enum):
    MEMORY = "memory"


class NotificationChannel(str, Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"


class NotificationStatus(str, Enum):
    SENT = "sent"
    FAILED = "failed"


@dataclass(frozen=True)
class NotificationRecipient:
    address: str
    name: str | None = None
    channel: NotificationChannel = NotificationChannel.EMAIL


@dataclass
class NotificationRequest:
    recipients: list[NotificationRecipient]
    subject: str
    body: str
    channel: NotificationChannel = NotificationChannel.EMAIL


@dataclass
class NotificationResponse:
    notification_id: str = field(default_factory=lambda: str(uuid4()))
    status: NotificationStatus = NotificationStatus.SENT
    provider: NotificationProviderType = NotificationProviderType.MEMORY
    error: str | None = None

    @property
    def delivered(self) -> bool:
        return self.status == NotificationStatus.SENT
