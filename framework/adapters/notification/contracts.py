from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from uuid import uuid4


class NotificationProviderType(str, Enum):
    MEMORY = "memory"
    SMTP = "smtp"
    SENDGRID = "sendgrid"
    MAILGUN = "mailgun"
    TWILIO = "twilio"
    SLACK = "slack"
    TEAMS = "teams"
    TELEGRAM = "telegram"
    FIREBASE = "firebase"
    WEB_PUSH = "web_push"


class NotificationChannel(str, Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    CHAT = "chat"
    WEBHOOK = "webhook"


class NotificationPriority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


class NotificationStatus(str, Enum):
    QUEUED = "queued"
    SENT = "sent"
    FAILED = "failed"


@dataclass(frozen=True)
class NotificationRecipient:
    address: str
    name: str | None = None
    channel: NotificationChannel = NotificationChannel.EMAIL
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class NotificationAttachment:
    filename: str
    content: bytes
    content_type: str = "application/octet-stream"


@dataclass(frozen=True)
class NotificationTemplate:
    key: str
    subject: str
    body: str


@dataclass
class NotificationRequest:
    recipients: list[NotificationRecipient]
    subject: str
    body: str
    channel: NotificationChannel = NotificationChannel.EMAIL
    priority: NotificationPriority = NotificationPriority.NORMAL
    attachments: list[NotificationAttachment] = field(default_factory=list)
    template: NotificationTemplate | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class NotificationResponse:
    notification_id: str = field(default_factory=lambda: str(uuid4()))
    status: NotificationStatus = NotificationStatus.QUEUED
    provider: NotificationProviderType = NotificationProviderType.MEMORY
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def delivered(self) -> bool:
        return self.status == NotificationStatus.SENT
