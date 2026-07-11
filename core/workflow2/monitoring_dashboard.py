from dataclasses import asdict

from core.workflow2.monitoring_service import WorkflowMonitoringService


class WorkflowMonitoringDashboard:
    def __init__(self, service: WorkflowMonitoringService) -> None:
        self.service = service

    def snapshot(self) -> dict[str, object]:
        summary = self.service.summary()
        return {
            "summary": asdict(summary),
            "health": self.service.health(),
            "active_instances": sorted(self.service.active_instances()),
        }
