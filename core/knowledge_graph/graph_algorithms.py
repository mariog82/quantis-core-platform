from collections import deque
from heapq import heappop, heappush
from math import inf
from time import perf_counter
from typing import Any

from core.knowledge_graph.algorithm_exceptions import (
    AlgorithmNodeNotFound,
    GraphContainsCycle,
    NegativeWeightNotSupported,
)
from core.knowledge_graph.algorithm_models import (
    CentralityResult,
    ConnectedComponentsResult,
    GraphAlgorithmMetrics,
    PathResult,
)
from core.knowledge_graph.identifiers import NodeId


def _node_id(node: Any) -> NodeId:
    return node.node_id


def _nodes(graph: Any) -> tuple[Any, ...]:
    return tuple(graph.nodes())


def _edges(graph: Any) -> tuple[Any, ...]:
    return tuple(graph.edges()) if hasattr(graph, "edges") else ()


def _neighbors(graph: Any, node_id: NodeId) -> tuple[Any, ...]:
    return tuple(graph.neighbors(node_id))


def _outgoing_edges(graph: Any, node_id: NodeId) -> tuple[Any, ...]:
    if hasattr(graph, "outgoing"):
        return tuple(graph.outgoing(node_id))
    return tuple(
        edge for edge in _edges(graph)
        if edge.source_id == node_id
        or (not getattr(edge, "directed", True) and edge.target_id == node_id)
    )


def _all_node_ids(graph: Any) -> tuple[NodeId, ...]:
    return tuple(_node_id(node) for node in _nodes(graph))


def _ensure_node(graph: Any, node_id: NodeId) -> None:
    if node_id not in set(_all_node_ids(graph)):
        raise AlgorithmNodeNotFound(node_id.value)


class GraphAlgorithmsService:
    def __init__(self, metrics: GraphAlgorithmMetrics | None = None) -> None:
        self.metrics = metrics or GraphAlgorithmMetrics()

    def _run(self, algorithm: str, operation):
        started = perf_counter()
        self.metrics.record(algorithm)
        try:
            return operation()
        except Exception:
            self.metrics.failures += 1
            raise
        finally:
            self.metrics.execution_time_seconds += perf_counter() - started

    def breadth_first(self, graph: Any, start_id: NodeId) -> tuple[NodeId, ...]:
        def operation() -> tuple[NodeId, ...]:
            _ensure_node(graph, start_id)
            visited = {start_id}
            order: list[NodeId] = []
            queue: deque[NodeId] = deque([start_id])
            while queue:
                current = queue.popleft()
                order.append(current)
                self.metrics.nodes_visited += 1
                for neighbor in _neighbors(graph, current):
                    neighbor_id = _node_id(neighbor)
                    self.metrics.edges_visited += 1
                    if neighbor_id not in visited:
                        visited.add(neighbor_id)
                        queue.append(neighbor_id)
            return tuple(order)
        return self._run("breadth_first", operation)

    def depth_first(self, graph: Any, start_id: NodeId) -> tuple[NodeId, ...]:
        def operation() -> tuple[NodeId, ...]:
            _ensure_node(graph, start_id)
            visited: set[NodeId] = set()
            order: list[NodeId] = []
            def visit(current: NodeId) -> None:
                visited.add(current)
                order.append(current)
                self.metrics.nodes_visited += 1
                for neighbor in _neighbors(graph, current):
                    neighbor_id = _node_id(neighbor)
                    self.metrics.edges_visited += 1
                    if neighbor_id not in visited:
                        visit(neighbor_id)
            visit(start_id)
            return tuple(order)
        return self._run("depth_first", operation)

    def shortest_path(self, graph: Any, source_id: NodeId, target_id: NodeId) -> PathResult:
        def operation() -> PathResult:
            _ensure_node(graph, source_id)
            _ensure_node(graph, target_id)
            queue: deque[NodeId] = deque([source_id])
            previous: dict[NodeId, NodeId | None] = {source_id: None}
            while queue:
                current = queue.popleft()
                self.metrics.nodes_visited += 1
                if current == target_id:
                    break
                for neighbor in _neighbors(graph, current):
                    neighbor_id = _node_id(neighbor)
                    self.metrics.edges_visited += 1
                    if neighbor_id not in previous:
                        previous[neighbor_id] = current
                        queue.append(neighbor_id)
            if target_id not in previous:
                return PathResult((), inf)
            path: list[NodeId] = []
            current: NodeId | None = target_id
            while current is not None:
                path.append(current)
                current = previous[current]
            path.reverse()
            return PathResult(tuple(path), float(len(path) - 1))
        return self._run("shortest_path", operation)

    def dijkstra(self, graph: Any, source_id: NodeId, target_id: NodeId) -> PathResult:
        def operation() -> PathResult:
            _ensure_node(graph, source_id)
            _ensure_node(graph, target_id)
            distances = {node_id: inf for node_id in _all_node_ids(graph)}
            distances[source_id] = 0.0
            previous: dict[NodeId, NodeId | None] = {source_id: None}
            queue: list[tuple[float, str, NodeId]] = [(0.0, source_id.value, source_id)]
            while queue:
                distance, _, current = heappop(queue)
                if distance != distances[current]:
                    continue
                self.metrics.nodes_visited += 1
                if current == target_id:
                    break
                for edge in _outgoing_edges(graph, current):
                    weight = float(getattr(edge, "weight", 1.0))
                    if weight < 0:
                        raise NegativeWeightNotSupported()
                    self.metrics.edges_visited += 1
                    neighbor = edge.target_id if edge.source_id == current else edge.source_id
                    candidate = distance + weight
                    if candidate < distances.get(neighbor, inf):
                        distances[neighbor] = candidate
                        previous[neighbor] = current
                        heappush(queue, (candidate, neighbor.value, neighbor))
            if distances[target_id] == inf:
                return PathResult((), inf)
            path: list[NodeId] = []
            current: NodeId | None = target_id
            while current is not None:
                path.append(current)
                current = previous[current]
            path.reverse()
            return PathResult(tuple(path), distances[target_id])
        return self._run("dijkstra", operation)

    def connected_components(self, graph: Any) -> ConnectedComponentsResult:
        def operation() -> ConnectedComponentsResult:
            remaining = set(_all_node_ids(graph))
            components: list[frozenset[NodeId]] = []
            while remaining:
                start = min(remaining, key=lambda item: item.value)
                component = set(self.breadth_first(graph, start))
                components.append(frozenset(component))
                remaining -= component
            return ConnectedComponentsResult(tuple(components))
        return self._run("connected_components", operation)

    def has_cycle(self, graph: Any) -> bool:
        def operation() -> bool:
            state = {node_id: 0 for node_id in _all_node_ids(graph)}
            def visit(current: NodeId) -> bool:
                state[current] = 1
                for edge in _outgoing_edges(graph, current):
                    neighbor = edge.target_id if edge.source_id == current else edge.source_id
                    if state.get(neighbor, 0) == 1:
                        return True
                    if state.get(neighbor, 0) == 0 and visit(neighbor):
                        return True
                state[current] = 2
                return False
            return any(state[node_id] == 0 and visit(node_id) for node_id in state)
        return self._run("has_cycle", operation)

    def topological_sort(self, graph: Any) -> tuple[NodeId, ...]:
        def operation() -> tuple[NodeId, ...]:
            node_ids = _all_node_ids(graph)
            indegree = {node_id: 0 for node_id in node_ids}
            adjacency = {node_id: [] for node_id in node_ids}
            for edge in _edges(graph):
                if not getattr(edge, "directed", True):
                    continue
                adjacency[edge.source_id].append(edge.target_id)
                indegree[edge.target_id] += 1
            queue = deque(sorted((n for n,d in indegree.items() if d == 0), key=lambda x:x.value))
            order: list[NodeId] = []
            while queue:
                current = queue.popleft()
                order.append(current)
                for neighbor in adjacency[current]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            if len(order) != len(node_ids):
                raise GraphContainsCycle()
            return tuple(order)
        return self._run("topological_sort", operation)

    def degree_centrality(self, graph: Any) -> CentralityResult:
        def operation() -> CentralityResult:
            node_ids = _all_node_ids(graph)
            denominator = max(len(node_ids) - 1, 1)
            return CentralityResult({n: len(_neighbors(graph, n)) / denominator for n in node_ids})
        return self._run("degree_centrality", operation)

    def closeness_centrality(self, graph: Any) -> CentralityResult:
        def operation() -> CentralityResult:
            values: dict[NodeId, float] = {}
            for source in _all_node_ids(graph):
                distances = self._distances(graph, source)
                reachable = [v for target,v in distances.items() if target != source and v < inf]
                values[source] = 0.0 if not reachable else len(reachable) / sum(reachable)
            return CentralityResult(values)
        return self._run("closeness_centrality", operation)

    def _distances(self, graph: Any, source_id: NodeId) -> dict[NodeId, float]:
        distances = {node_id: inf for node_id in _all_node_ids(graph)}
        distances[source_id] = 0.0
        queue: deque[NodeId] = deque([source_id])
        while queue:
            current = queue.popleft()
            for neighbor in _neighbors(graph, current):
                neighbor_id = _node_id(neighbor)
                if distances[neighbor_id] == inf:
                    distances[neighbor_id] = distances[current] + 1.0
                    queue.append(neighbor_id)
        return distances
