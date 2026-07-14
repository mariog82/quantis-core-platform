from dataclasses import dataclass, field

from core.knowledge_graph.identifiers import NodeId


@dataclass(frozen=True)
class PathResult:
    nodes: tuple[NodeId, ...]
    total_weight: float

    @property
    def found(self) -> bool:
        return bool(self.nodes)


@dataclass(frozen=True)
class CentralityResult:
    values: dict[NodeId, float]


@dataclass(frozen=True)
class ConnectedComponentsResult:
    components: tuple[frozenset[NodeId], ...]


@dataclass
class GraphAlgorithmMetrics:
    executions: int = 0
    failures: int = 0
    nodes_visited: int = 0
    edges_visited: int = 0
    execution_time_seconds: float = 0.0
    algorithm_counts: dict[str, int] = field(default_factory=dict)

    def record(self, algorithm: str) -> None:
        self.executions += 1
        self.algorithm_counts[algorithm] = self.algorithm_counts.get(algorithm, 0) + 1
