from dataclasses import dataclass, field
from xml.etree import ElementTree as ET

from core.workflow2.bpmn import BPMN_NS


@dataclass(frozen=True)
class BPMNValidationIssue:
    code: str
    message: str


@dataclass
class BPMNValidationReport:
    issues: list[BPMNValidationIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def add(self, code: str, message: str) -> None:
        self.issues.append(BPMNValidationIssue(code, message))


BPMNValidationIssue.__test__ = False
BPMNValidationReport.__test__ = False


class BPMNValidator:
    def validate(self, xml_text: str) -> BPMNValidationReport:
        report = BPMNValidationReport()

        try:
            root = ET.fromstring(xml_text)
        except ET.ParseError as exc:
            report.add("INVALID_XML", str(exc))
            return report

        process = root.find(f".//{{{BPMN_NS}}}process")
        if process is None:
            report.add("MISSING_PROCESS", "BPMN process element is required")
            return report

        if not process.attrib.get("id", "").strip():
            report.add("MISSING_PROCESS_ID", "BPMN process id is required")

        start_events = process.findall(f"{{{BPMN_NS}}}startEvent")
        if len(start_events) != 1:
            report.add(
                "INVALID_START_EVENT_COUNT",
                "Exactly one startEvent is required",
            )

        element_ids = {
            element.attrib.get("id")
            for element in list(process)
            if element.attrib.get("id")
        }

        for flow in process.findall(f"{{{BPMN_NS}}}sequenceFlow"):
            source = flow.attrib.get("sourceRef")
            target = flow.attrib.get("targetRef")
            if source not in element_ids:
                report.add("UNKNOWN_SOURCE_REF", str(source))
            if target not in element_ids:
                report.add("UNKNOWN_TARGET_REF", str(target))

        return report
