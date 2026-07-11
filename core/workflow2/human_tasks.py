from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


class HumanTaskStatus(str, Enum):
    CREATED = "created"
    CLAIMED = "claimed"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    RELEASED = "released"
    DELEGATED = "delegated"
    CANCELLED = "cancelled"
    EXPIRED = "expired"


class HumanTaskPriority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class HumanTaskId:
    value: str = field(default_factory=lambda: str(uuid4()))


@dataclass(frozen=True)
class HumanTask:
    workflow_instance_id: str
    step_id: str
    name: str
    task_id: HumanTaskId = field(default_factory=HumanTaskId)
    assignee_id: str | None = None
    candidate_users: tuple[str, ...] = ()
    candidate_groups: tuple[str, ...] = ()
    status: HumanTaskStatus = HumanTaskStatus.CREATED
    priority: HumanTaskPriority = HumanTaskPriority.NORMAL
    due_at: datetime | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None
    payload: dict[str, Any] = field(default_factory=dict)
    result: dict[str, Any] = field(default_factory=dict)
    delegated_from: str | None = None

    def claim(self, user_id: str) -> "HumanTask":
        if self.status not in {
            HumanTaskStatus.CREATED,
            HumanTaskStatus.RELEASED,
            HumanTaskStatus.DELEGATED,
        }:
            raise ValueError("Task cannot be claimed in its current state")

        if self.candidate_users and user_id not in self.candidate_users:
            raise PermissionError("User is not a candidate for this task")

        return replace(
            self,
            assignee_id=user_id,
            status=HumanTaskStatus.CLAIMED,
        )

    def start(self, user_id: str) -> "HumanTask":
        if self.assignee_id != user_id:
            raise PermissionError("Only the assignee can start the task")
        if self.status != HumanTaskStatus.CLAIMED:
            raise ValueError("Task must be claimed before starting")

        return replace(
            self,
            status=HumanTaskStatus.IN_PROGRESS,
        )

    def complete(
        self,
        user_id: str,
        result: dict[str, Any] | None = None,
    ) -> "HumanTask":
        if self.assignee_id != user_id:
            raise PermissionError("Only the assignee can complete the task")
        if self.status not in {
            HumanTaskStatus.CLAIMED,
            HumanTaskStatus.IN_PROGRESS,
        }:
            raise ValueError("Task is not completable")

        return replace(
            self,
            status=HumanTaskStatus.COMPLETED,
            result=dict(result or {}),
            completed_at=datetime.now(timezone.utc),
        )

    def release(self, user_id: str) -> "HumanTask":
        if self.assignee_id != user_id:
            raise PermissionError("Only the assignee can release the task")

        return replace(
            self,
            assignee_id=None,
            status=HumanTaskStatus.RELEASED,
        )

    def delegate(self, from_user_id: str, to_user_id: str) -> "HumanTask":
        if self.assignee_id != from_user_id:
            raise PermissionError("Only the assignee can delegate the task")

        return replace(
            self,
            assignee_id=to_user_id,
            delegated_from=from_user_id,
            status=HumanTaskStatus.DELEGATED,
        )
