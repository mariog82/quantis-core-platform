from dataclasses import dataclass


@dataclass
class GraphQueryMetrics:
    executions: int = 0
    failures: int = 0
    nodes_scanned: int = 0
    edges_scanned: int = 0
    cache_hits: int = 0
    cache_misses: int = 0
    execution_time_seconds: float = 0.0


__all__ = ["GraphQueryMetrics"]
