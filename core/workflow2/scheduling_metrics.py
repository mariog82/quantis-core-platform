from dataclasses import dataclass


@dataclass
class WorkflowSchedulingMetrics:
    scheduled: int = 0
    fired: int = 0
    cancelled: int = 0
    expired: int = 0
    scheduler_failures: int = 0
