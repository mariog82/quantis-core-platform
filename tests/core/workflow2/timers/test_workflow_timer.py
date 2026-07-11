from datetime import datetime, timedelta, timezone

import pytest

from core.workflow2 import TimerStatus, WorkflowTimer


def test_workflow_timer_fires_when_due():
    now = datetime.now(timezone.utc)
    timer = WorkflowTimer(
        workflow_instance_id="wf-1",
        step_id="wait",
        fire_at=now - timedelta(seconds=1),
    )

    fired = timer.fire(now)

    assert fired.status == TimerStatus.FIRED
    assert fired.fired_at == now


def test_workflow_timer_rejects_early_fire():
    now = datetime.now(timezone.utc)
    timer = WorkflowTimer(
        workflow_instance_id="wf-1",
        step_id="wait",
        fire_at=now + timedelta(seconds=10),
    )

    with pytest.raises(ValueError):
        timer.fire(now)
