from dataclasses import dataclass


@dataclass
class DeadLetterMetrics:
    added: int = 0
    replayed: int = 0
    removed: int = 0
    replay_failures: int = 0
