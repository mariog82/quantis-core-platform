from core.workflow2 import BPMNValidator


def test_bpmn_validator_rejects_missing_start_event():
    xml_text = '''<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL">
      <bpmn:process id="broken"/>
    </bpmn:definitions>'''

    report = BPMNValidator().validate(xml_text)

    assert report.passed is False
    assert "INVALID_START_EVENT_COUNT" in {
        issue.code for issue in report.issues
    }
