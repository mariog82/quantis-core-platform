import pytest

from framework.workflow import (
    Workflow,
    WorkflowContext,
    WorkflowEngine,
    WorkflowExecutionStatus,
    WorkflowId,
    WorkflowStep,
    WorkflowStepError,
)


def add_value(context: WorkflowContext) -> WorkflowContext:
    context.data["value"] = 1
    return context


def fail_step(context: WorkflowContext) -> WorkflowContext:
    raise RuntimeError("step failed")


def test_workflow_engine_executes_steps():
    workflow = Workflow(id=WorkflowId(), name="demo")
    workflow.add_step(WorkflowStep(name="add-value", handler=add_value))

    engine = WorkflowEngine()
    engine.register(workflow)

    execution = engine.execute("demo", WorkflowContext(tenant_id="tenant-demo"))

    assert execution.status == WorkflowExecutionStatus.COMPLETED
    assert execution.context.data["value"] == 1
    assert execution.executed_steps == ["add-value"]


def test_workflow_engine_fails_on_step_error():
    workflow = Workflow(id=WorkflowId(), name="broken")
    workflow.add_step(WorkflowStep(name="fail", handler=fail_step))

    engine = WorkflowEngine()
    engine.register(workflow)

    with pytest.raises(WorkflowStepError):
        engine.execute("broken")
