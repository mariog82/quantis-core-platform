from core.event import RetryPolicy


def test_retry_policy_and_backoff():
    policy = RetryPolicy(
        max_attempts=3,
        initial_backoff_seconds=0.5,
        multiplier=2.0,
        max_backoff_seconds=2.0,
    )

    assert policy.should_retry(2) is True
    assert policy.should_retry(3) is False
    assert policy.backoff_seconds(1) == 0.5
    assert policy.backoff_seconds(2) == 1.0
    assert policy.backoff_seconds(3) == 2.0
    assert policy.backoff_seconds(4) == 2.0
