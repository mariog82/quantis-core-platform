from dataclasses import dataclass
from typing import Protocol
from xml.etree import ElementTree as ET

from core.workflow2.definition import (
    WorkflowDefinition,
    WorkflowStepDefinition,
    WorkflowTransition,
)


BPMN_NS = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(frozen=True)
class BPMNImportResult:
    definition: WorkflowDefinition
    source_xml: str


class BPMNParser(Protocol):
    def parse(self, xml_text: str) -> BPMNImportResult:
        ...


class SimpleBPMNParser:
    def parse(self, xml_text: str) -> BPMNImportResult:
        root = ET.fromstring(xml_text)
        process = root.find(f".//{{{BPMN_NS}}}process")
        if process is None:
            raise ValueError("BPMN process element not found")

        workflow_id = process.attrib.get("id", "").strip()
        if not workflow_id:
            raise ValueError("BPMN process id is required")

        name = process.attrib.get("name", workflow_id)
        steps: list[WorkflowStepDefinition] = []
        transitions: list[WorkflowTransition] = []
        initial_step_id: str | None = None

        supported_steps = {
            "startEvent": "start",
            "endEvent": "end",
            "serviceTask": "service",
            "userTask": "human",
            "scriptTask": "script",
            "intermediateCatchEvent": "timer",
            "exclusiveGateway": "gateway",
            "parallelGateway": "gateway",
        }

        for tag_name, step_type in supported_steps.items():
            for element in process.findall(f"{{{BPMN_NS}}}{tag_name}"):
                step_id = element.attrib.get("id", "").strip()
                if not step_id:
                    raise ValueError(f"BPMN {tag_name} requires id")
                steps.append(
                    WorkflowStepDefinition(
                        step_id=step_id,
                        name=element.attrib.get("name", step_id),
                        step_type=step_type,
                        metadata={"bpmn_type": tag_name},
                    )
                )
                if tag_name == "startEvent" and initial_step_id is None:
                    initial_step_id = step_id

        for flow in process.findall(f"{{{BPMN_NS}}}sequenceFlow"):
            source = flow.attrib.get("sourceRef", "").strip()
            target = flow.attrib.get("targetRef", "").strip()
            if not source or not target:
                raise ValueError("BPMN sequenceFlow requires sourceRef and targetRef")
            transitions.append(
                WorkflowTransition(
                    source_step_id=source,
                    target_step_id=target,
                    condition=flow.attrib.get("name"),
                    metadata={"bpmn_id": flow.attrib.get("id", "")},
                )
            )

        if initial_step_id is None:
            raise ValueError("BPMN startEvent is required")

        definition = WorkflowDefinition(
            workflow_id=workflow_id,
            version=1,
            name=name,
            initial_step_id=initial_step_id,
            steps=tuple(steps),
            transitions=tuple(transitions),
            metadata={"source": "bpmn"},
        )
        return BPMNImportResult(definition=definition, source_xml=xml_text)
