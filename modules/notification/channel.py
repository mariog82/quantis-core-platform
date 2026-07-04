from abc import ABC, abstractmethod

from modules.notification.message import NotificationMessage


class NotificationChannel(ABC):
    name: str

    @abstractmethod
    def send(self, message: NotificationMessage) -> bool:
        raise NotImplementedError


class InMemoryNotificationChannel(NotificationChannel):
    name = "memory"

    def __init__(self):
        self.messages: list[NotificationMessage] = []

    def send(self, message: NotificationMessage) -> bool:
        self.messages.append(message)
        return True
