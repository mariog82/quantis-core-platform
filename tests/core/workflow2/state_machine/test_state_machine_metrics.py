from core.workflow2 import StateMachineMetrics


def test_state_machine_metrics_defaults():
    metrics = StateMachineMetrics()

    assert metrics.transitions_evaluated == 0
    assert metrics.transitions_allowed == 0
    assert metrics.transitions_rejected == 0
    assert metrics.guards_evaluated == 0
    assert metrics.guards_failed == 0
