from dataclasses import dataclass


@dataclass
class WorkflowRuntimeMetrics:
    instances_created: int = 0
    steps_executed: int = 0
    steps_failed: int = 0
    instances_completed: int = 0
    instances_waiting: int = 0
