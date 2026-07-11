from datetime import datetime, timedelta, timezone

from core.workflow2 import (
    InMemoryWorkflowTimerRepository,
    TimerStatus,
    WorkflowScheduler,
    WorkflowTimer,
)


def test_scheduler_cancels_timer():
    scheduler = WorkflowScheduler(InMemoryWorkflowTimerRepository())
    timer = scheduler.schedule(
        WorkflowTimer(
            workflow_instance_id="wf-1",
            step_id="wait",
            fire_at=datetime.now(timezone.utc) + timedelta(minutes=5),
        )
    )

    cancelled = scheduler.cancel(timer.timer_id)

    assert cancelled.status == TimerStatus.CANCELLED
    assert scheduler.pending_for_instance("wf-1") == []
