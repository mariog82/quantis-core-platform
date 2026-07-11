from dataclasses import dataclass

from core.workflow2.bpmn import BPMNImportResult, SimpleBPMNParser
from core.workflow2.bpmn_validation import BPMNValidator
from core.workflow2.exceptions import InvalidWorkflowDefinition
from core.workflow2.registry import WorkflowRegistry


@dataclass
class BPMNWorkflowImporter:
    registry: WorkflowRegistry
    parser: SimpleBPMNParser
    validator: BPMNValidator

    def import_xml(self, xml_text: str) -> BPMNImportResult:
        report = self.validator.validate(xml_text)
        if not report.passed:
            raise InvalidWorkflowDefinition(
                ", ".join(issue.code for issue in report.issues)
            )

        result = self.parser.parse(xml_text)
        self.registry.register(result.definition)
        return result
