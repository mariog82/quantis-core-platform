from dataclasses import dataclass


@dataclass
class StateMachineMetrics:
    transitions_evaluated: int = 0
    transitions_allowed: int = 0
    transitions_rejected: int = 0
    guards_evaluated: int = 0
    guards_failed: int = 0
