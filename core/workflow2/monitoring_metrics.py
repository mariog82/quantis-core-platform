from dataclasses import dataclass


@dataclass
class WorkflowMonitoringMetrics:
    events_recorded: int = 0
    snapshots_generated: int = 0
    active_instances: int = 0
    completed_instances: int = 0
    failed_instances: int = 0
    monitoring_failures: int = 0
