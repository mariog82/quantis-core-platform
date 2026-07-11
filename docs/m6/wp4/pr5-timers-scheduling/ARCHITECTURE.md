# Timers and Scheduling Architecture

```text
Timer workflow step
      ↓
TimerStepExecutor
      ↓
WorkflowScheduler
      ↓
WorkflowTimerRepository
      ↓
Scheduled timer
      ↓
fire_due()
      ↓
WorkflowTimer.FIRED
```
