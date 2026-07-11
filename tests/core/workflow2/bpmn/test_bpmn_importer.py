from core.workflow2 import (
    BPMNWorkflowImporter,
    BPMNValidator,
    InMemoryWorkflowRegistry,
    SimpleBPMNParser,
)


def test_bpmn_importer_registers_definition():
    xml_text = '''<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL">
      <bpmn:process id="simple.flow" name="Simple">
        <bpmn:startEvent id="start"/>
        <bpmn:endEvent id="end"/>
        <bpmn:sequenceFlow id="f1" sourceRef="start" targetRef="end"/>
      </bpmn:process>
    </bpmn:definitions>'''

    registry = InMemoryWorkflowRegistry()
    importer = BPMNWorkflowImporter(
        registry=registry,
        parser=SimpleBPMNParser(),
        validator=BPMNValidator(),
    )

    result = importer.import_xml(xml_text)

    assert registry.latest("simple.flow") == result.definition
