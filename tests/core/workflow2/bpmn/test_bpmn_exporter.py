from core.workflow2 import (
    BPMNExporter,
    SimpleBPMNParser,
    WorkflowDefinition,
    WorkflowStepDefinition,
    WorkflowTransition,
)


def test_bpmn_exporter_roundtrip():
    definition = WorkflowDefinition(
        workflow_id="tenant.provisioning",
        version=1,
        name="Tenant Provisioning",
        initial_step_id="start",
        steps=(
            WorkflowStepDefinition("start", "Start", step_type="start"),
            WorkflowStepDefinition("create", "Create", step_type="service"),
            WorkflowStepDefinition("end", "End", step_type="end"),
        ),
        transitions=(
            WorkflowTransition("start", "create"),
            WorkflowTransition("create", "end"),
        ),
    )

    xml_text = BPMNExporter().export(definition)
    restored = SimpleBPMNParser().parse(xml_text).definition

    assert restored.workflow_id == definition.workflow_id
    assert restored.initial_step_id == "start"
    assert len(restored.steps) == 3
