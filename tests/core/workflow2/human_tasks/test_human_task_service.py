from core.workflow2 import (
    HumanTask,
    HumanTaskService,
    InMemoryHumanTaskRepository,
)


def test_human_task_service_claim_release_delegate():
    repository = InMemoryHumanTaskRepository()
    service = HumanTaskService(repository)

    task = service.create(
        HumanTask(
            workflow_instance_id="wf-1",
            step_id="review",
            name="Review",
        )
    )

    claimed = service.claim(task.task_id, "u1")
    released = service.release(task.task_id, "u1")
    claimed_again = service.claim(task.task_id, "u2")
    delegated = service.delegate(task.task_id, "u2", "u3")

    assert claimed.assignee_id == "u1"
    assert released.assignee_id is None
    assert claimed_again.assignee_id == "u2"
    assert delegated.assignee_id == "u3"
    assert delegated.delegated_from == "u2"
