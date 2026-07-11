from dataclasses import dataclass


@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int = 3
    initial_backoff_seconds: float = 0.1
    multiplier: float = 2.0
    max_backoff_seconds: float = 30.0

    def should_retry(self, attempts: int) -> bool:
        return attempts < self.max_attempts

    def backoff_seconds(self, attempts: int) -> float:
        if attempts <= 0:
            return 0.0

        value = self.initial_backoff_seconds * (
            self.multiplier ** (attempts - 1)
        )

        return min(value, self.max_backoff_seconds)