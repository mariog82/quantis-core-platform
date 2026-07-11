from core.workflow2 import BPMNMetrics


def test_bpmn_metrics_defaults():
    metrics = BPMNMetrics()

    assert metrics.documents_imported == 0
    assert metrics.documents_exported == 0
    assert metrics.validation_failures == 0
    assert metrics.parse_failures == 0
