from dataclasses import dataclass


@dataclass
class HumanTaskMetrics:
    created: int = 0
    claimed: int = 0
    started: int = 0
    completed: int = 0
    released: int = 0
    delegated: int = 0
    expired: int = 0
