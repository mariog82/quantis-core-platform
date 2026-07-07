from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable
from uuid import uuid4

class MessagingProviderType(str, Enum):
    MEMORY = "memory"
    RABBITMQ = "rabbitmq"
    KAFKA = "kafka"
    REDIS_STREAMS = "redis_streams"
    SQS = "sqs"
    AZURE_QUEUE = "azure_queue"

class MessagePriority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class Message:
    payload: Any
    headers: dict[str, str] = field(default_factory=dict)
    priority: MessagePriority = MessagePriority.NORMAL

@dataclass
class MessageEnvelope:
    topic: str
    message: Message
    message_id: str = field(default_factory=lambda: str(uuid4()))
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class MessagePublishRequest:
    topic: str
    message: Message

MessageHandler = Callable[[MessageEnvelope], None]

@dataclass
class MessageSubscribeRequest:
    topic: str
    handler: MessageHandler

@dataclass
class MessageAcknowledgement:
    message_id: str
    accepted: bool = True
    error: str | None = None
