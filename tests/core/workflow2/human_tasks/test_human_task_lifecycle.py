from core.workflow2 import (
    HumanTask,
    HumanTaskStatus,
)


def test_human_task_lifecycle():
    task = HumanTask(
        workflow_instance_id="wf-1",
        step_id="review",
        name="Review document",
        candidate_users=("u1", "u2"),
    )

    claimed = task.claim("u1")
    started = claimed.start("u1")
    completed = started.complete(
        "u1",
        {"approved": True},
    )

    assert claimed.status == HumanTaskStatus.CLAIMED
    assert started.status == HumanTaskStatus.IN_PROGRESS
    assert completed.status == HumanTaskStatus.COMPLETED
    assert completed.result == {"approved": True}
    assert completed.completed_at is not None
