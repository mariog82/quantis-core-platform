from framework.workflow import Workflow, WorkflowId, WorkflowRegistry


def test_register_and_get_workflow():
    registry = WorkflowRegistry()
    workflow = Workflow(id=WorkflowId(), name="demo-workflow")

    registry.register(workflow)

    assert registry.exists("demo-workflow")
    assert registry.get("demo-workflow") == workflow


def test_list_workflows():
    registry = WorkflowRegistry()
    registry.register(Workflow(id=WorkflowId(), name="a"))
    registry.register(Workflow(id=WorkflowId(), name="b"))

    assert len(registry.list_workflows()) == 2
