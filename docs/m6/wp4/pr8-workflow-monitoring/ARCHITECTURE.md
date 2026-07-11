# Workflow Monitoring Architecture

```text
Workflow Runtime / Human Tasks / Timers / Saga
                    ↓
        WorkflowMonitoringEvent
                    ↓
        WorkflowMonitoringSink
                    ↓
       WorkflowMonitoringService
          ├── history
          ├── active instances
          ├── KPI summary
          └── health
                    ↓
      WorkflowMonitoringDashboard
```
