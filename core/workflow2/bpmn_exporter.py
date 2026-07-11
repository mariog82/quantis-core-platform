from xml.etree import ElementTree as ET

from core.workflow2.definition import WorkflowDefinition
from core.workflow2.bpmn import BPMN_NS


class BPMNExporter:
    _STEP_TAGS = {
        "start": "startEvent",
        "end": "endEvent",
        "service": "serviceTask",
        "human": "userTask",
        "script": "scriptTask",
        "timer": "intermediateCatchEvent",
        "gateway": "exclusiveGateway",
    }

    def export(self, definition: WorkflowDefinition) -> str:
        definitions = ET.Element(
            f"{{{BPMN_NS}}}definitions",
            attrib={"id": f"{definition.workflow_id}-definitions"},
        )
        process = ET.SubElement(
            definitions,
            f"{{{BPMN_NS}}}process",
            attrib={
                "id": definition.workflow_id,
                "name": definition.name,
                "isExecutable": "true",
            },
        )

        for step in definition.steps:
            tag_name = self._STEP_TAGS.get(step.step_type, "serviceTask")
            ET.SubElement(
                process,
                f"{{{BPMN_NS}}}{tag_name}",
                attrib={
                    "id": step.step_id,
                    "name": step.name,
                },
            )

        for index, transition in enumerate(definition.transitions, start=1):
            attributes = {
                "id": transition.metadata.get("bpmn_id") or f"flow-{index}",
                "sourceRef": transition.source_step_id,
                "targetRef": transition.target_step_id,
            }
            if transition.condition:
                attributes["name"] = transition.condition

            ET.SubElement(
                process,
                f"{{{BPMN_NS}}}sequenceFlow",
                attrib=attributes,
            )

        ET.register_namespace("bpmn", BPMN_NS)
        return ET.tostring(definitions, encoding="unicode")
