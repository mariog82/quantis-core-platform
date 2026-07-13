from dataclasses import dataclass

@dataclass
class GraphRepositoryMetrics:
    saves: int = 0
    loads: int = 0
    deletes: int = 0
    snapshots: int = 0
    restores: int = 0
    failures: int = 0
