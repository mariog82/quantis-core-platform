from core.event import DeadLetterMetrics


def test_deadletter_metrics_defaults():
    metrics = DeadLetterMetrics()

    assert metrics.added == 0
    assert metrics.replayed == 0
    assert metrics.removed == 0
    assert metrics.replay_failures == 0
