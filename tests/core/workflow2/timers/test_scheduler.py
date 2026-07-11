from datetime import datetime, timedelta, timezone

from core.workflow2 import (
    InMemoryWorkflowTimerRepository,
    TimerStatus,
    WorkflowScheduler,
    WorkflowTimer,
)


def test_scheduler_fires_due_timers_only():
    now = datetime.now(timezone.utc)
    repository = InMemoryWorkflowTimerRepository()
    scheduler = WorkflowScheduler(repository)

    due = scheduler.schedule(
        WorkflowTimer(
            workflow_instance_id="wf-1",
            step_id="due",
            fire_at=now - timedelta(seconds=1),
        )
    )
    scheduler.schedule(
        WorkflowTimer(
            workflow_instance_id="wf-1",
            step_id="future",
            fire_at=now + timedelta(seconds=60),
        )
    )

    fired = scheduler.fire_due(now)

    assert len(fired) == 1
    assert fired[0].timer_id == due.timer_id
    assert fired[0].status == TimerStatus.FIRED
