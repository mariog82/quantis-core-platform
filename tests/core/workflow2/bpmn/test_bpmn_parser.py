from core.workflow2 import SimpleBPMNParser


BPMN_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL">
  <bpmn:process id="document.approval" name="Document Approval">
    <bpmn:startEvent id="start" name="Start"/>
    <bpmn:userTask id="review" name="Review"/>
    <bpmn:endEvent id="end" name="End"/>
    <bpmn:sequenceFlow id="f1" sourceRef="start" targetRef="review"/>
    <bpmn:sequenceFlow id="f2" sourceRef="review" targetRef="end"/>
  </bpmn:process>
</bpmn:definitions>
'''


def test_bpmn_parser_builds_workflow_definition():
    result = SimpleBPMNParser().parse(BPMN_XML)

    assert result.definition.workflow_id == "document.approval"
    assert result.definition.initial_step_id == "start"
    assert result.definition.step("review").step_type == "human"
    assert len(result.definition.transitions) == 2
