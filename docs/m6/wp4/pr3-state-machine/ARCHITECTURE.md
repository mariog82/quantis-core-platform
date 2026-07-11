# State Machine Architecture

```text
WorkflowInstance
      ↓
WorkflowStateMachine.can_transition()
      ↓
WorkflowTransition
      ↓
Guard evaluation
      ↓
StateMachineDecision
      ↓
WorkflowInstance.move_to()
```
