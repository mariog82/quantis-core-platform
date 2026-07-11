from dataclasses import dataclass, field, replace
from datetime import datetime, timedelta, timezone
from enum import Enum
from uuid import uuid4


class TimerStatus(str, Enum):
    SCHEDULED = "scheduled"
    FIRED = "fired"
    CANCELLED = "cancelled"
    EXPIRED = "expired"


class TimerType(str, Enum):
    DELAY = "delay"
    DEADLINE = "deadline"
    REMINDER = "reminder"


@dataclass(frozen=True)
class WorkflowTimerId:
    value: str = field(default_factory=lambda: str(uuid4()))


@dataclass(frozen=True)
class WorkflowTimer:
    workflow_instance_id: str
    step_id: str
    fire_at: datetime
    timer_type: TimerType = TimerType.DELAY
    timer_id: WorkflowTimerId = field(default_factory=WorkflowTimerId)
    status: TimerStatus = TimerStatus.SCHEDULED
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    fired_at: datetime | None = None
    payload: dict[str, object] = field(default_factory=dict)

    def fire(self, now: datetime | None = None) -> "WorkflowTimer":
        current = now or datetime.now(timezone.utc)
        if self.status != TimerStatus.SCHEDULED:
            raise ValueError("Only scheduled timers can fire")
        if current < self.fire_at:
            raise ValueError("Timer is not due yet")

        return replace(
            self,
            status=TimerStatus.FIRED,
            fired_at=current,
        )

    def cancel(self) -> "WorkflowTimer":
        if self.status != TimerStatus.SCHEDULED:
            raise ValueError("Only scheduled timers can be cancelled")
        return replace(self, status=TimerStatus.CANCELLED)

    def is_due(self, now: datetime | None = None) -> bool:
        current = now or datetime.now(timezone.utc)
        return self.status == TimerStatus.SCHEDULED and current >= self.fire_at


@dataclass(frozen=True)
class Delay:
    seconds: float

    def fire_at(self, now: datetime | None = None) -> datetime:
        current = now or datetime.now(timezone.utc)
        return current + timedelta(seconds=self.seconds)
