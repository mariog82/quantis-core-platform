from core.workflow2.openapi import build_workflow_openapi


def test_workflow_openapi_contains_required_operations():
    spec = build_workflow_openapi()

    assert spec["openapi"] == "3.1.0"
    assert "/workflows" in spec["paths"]
    assert "/workflow-instances" in spec["paths"]
    assert "/human-tasks/{task_id}/complete" in spec["paths"]
