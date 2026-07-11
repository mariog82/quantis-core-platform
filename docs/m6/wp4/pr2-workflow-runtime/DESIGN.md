# Design Notes

The runtime is transport-neutral and executor-driven.

Step execution returns immutable `StepResult` values, allowing deterministic workflow state transitions.
