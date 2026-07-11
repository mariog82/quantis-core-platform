import pytest

from core.workflow2 import HumanTask


def test_non_candidate_cannot_claim():
    task = HumanTask(
        workflow_instance_id="wf-1",
        step_id="review",
        name="Review",
        candidate_users=("u1",),
    )

    with pytest.raises(PermissionError):
        task.claim("u2")
