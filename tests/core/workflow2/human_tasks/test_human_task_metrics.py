from core.workflow2 import HumanTaskMetrics


def test_human_task_metrics_defaults():
    metrics = HumanTaskMetrics()

    assert metrics.created == 0
    assert metrics.claimed == 0
    assert metrics.started == 0
    assert metrics.completed == 0
    assert metrics.released == 0
    assert metrics.delegated == 0
    assert metrics.expired == 0
