from collections import deque

from core.knowledge_graph.graph import KnowledgeGraph
from core.knowledge_graph.identifiers import NodeId
from core.knowledge_graph.query_models import QueryDirection


class GraphTraversalQuery:
    def neighbors(
        self,
        graph: KnowledgeGraph,
        node_id: NodeId,
        *,
        direction: QueryDirection = QueryDirection.ANY,
    ):
        if direction == QueryDirection.OUTGOING:
            target_ids = {
                edge.target_id
                for edge in graph.outgoing(node_id)
            }

        elif direction == QueryDirection.INCOMING:
            target_ids = {
                edge.source_id
                for edge in graph.incoming(node_id)
            }

        else:
            return graph.neighbors(node_id)

        return tuple(
            graph.get_node(current)
            for current in sorted(
                target_ids,
                key=lambda value: value.value,
            )
        )

    def breadth_first(
        self,
        graph: KnowledgeGraph,
        start_id: NodeId,
        *,
        max_depth: int = 1,
    ) -> tuple[NodeId, ...]:
        visited = {start_id}
        result: list[NodeId] = []
        queue: deque[tuple[NodeId, int]] = deque(
            [(start_id, 0)]
        )

        while queue:
            current, depth = queue.popleft()

            if depth >= max_depth:
                continue

            for neighbor in graph.neighbors(current):
                neighbor_id = neighbor.node_id

                if neighbor_id not in visited:
                    visited.add(neighbor_id)
                    result.append(neighbor_id)
                    queue.append((neighbor_id, depth + 1))

        return tuple(result)

    def depth_first(
        self,
        graph: KnowledgeGraph,
        start_id: NodeId,
        *,
        max_depth: int = 1,
    ) -> tuple[NodeId, ...]:
        visited = {start_id}
        result: list[NodeId] = []

        def visit(current: NodeId, depth: int) -> None:
            if depth >= max_depth:
                return

            for neighbor in graph.neighbors(current):
                neighbor_id = neighbor.node_id

                if neighbor_id not in visited:
                    visited.add(neighbor_id)
                    result.append(neighbor_id)
                    visit(neighbor_id, depth + 1)

        visit(start_id, 0)
        return tuple(result)


__all__ = ["GraphTraversalQuery"]
