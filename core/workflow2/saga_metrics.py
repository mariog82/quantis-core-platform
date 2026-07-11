from dataclasses import dataclass


@dataclass
class SagaMetrics:
    started: int = 0
    completed: int = 0
    failed: int = 0
    compensations_started: int = 0
    compensations_completed: int = 0
    compensation_failures: int = 0
