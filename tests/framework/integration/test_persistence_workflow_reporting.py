from dataclasses import dataclass

from framework.persistence import InMemoryRepository, UnitOfWork, UnitOfWorkState
from framework.reporting import ReportContext, ReportDefinition, ReportId, ReportingRuntime
from framework.workflow import Workflow, WorkflowContext, WorkflowEngine, WorkflowId, WorkflowStep


@dataclass
class Item:
    id: str
    name: str


def test_persistence_workflow_reporting_integration():
    repository = InMemoryRepository[Item, str]()
    repository.save(Item(id="1", name="Alpha"))

    def load_item(context: WorkflowContext) -> WorkflowContext:
        item = repository.get("1")
        context.data["item_name"] = item.name
        return context

    workflow = Workflow(id=WorkflowId(), name="load-item")
    workflow.add_step(WorkflowStep(name="load", handler=load_item))

    engine = WorkflowEngine()
    engine.register(workflow)
    execution = engine.execute("load-item")

    def report_provider(context: ReportContext) -> dict:
        return {"item_name": execution.context.data["item_name"]}

    reporting = ReportingRuntime()
    reporting.register(
        ReportDefinition(
            id=ReportId(),
            name="item-report",
            title="Item Report",
            provider=report_provider,
        )
    )

    with UnitOfWork() as uow:
        uow.register_new({"report": "item-report"})

    assert uow.state == UnitOfWorkState.COMMITTED
    assert b"Alpha" in reporting.generate("item-report").content
