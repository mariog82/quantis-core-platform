from dataclasses import dataclass


@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int = 3
    backoff_seconds: float = 0.1

    def should_retry(self, attempts: int) -> bool:
        return attempts < self.max_attempts
