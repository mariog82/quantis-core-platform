from dataclasses import replace
from core.knowledge_graph.exceptions import DuplicateEdge, DuplicateNode, EdgeNotFound, NodeNotFound
from core.knowledge_graph.identifiers import EdgeId, NodeId
from core.knowledge_graph.models import GraphEdge, GraphNode

class KnowledgeGraph:
    def __init__(self) -> None:
        self._nodes: dict[NodeId, GraphNode] = {}
        self._edges: dict[EdgeId, GraphEdge] = {}

    def add_node(self, node: GraphNode) -> GraphNode:
        if node.node_id in self._nodes:
            raise DuplicateNode(node.node_id.value)
        self._nodes[node.node_id] = node
        return node

    def add_edge(self, edge: GraphEdge) -> GraphEdge:
        if edge.edge_id in self._edges:
            raise DuplicateEdge(edge.edge_id.value)
        if edge.source_id not in self._nodes:
            raise NodeNotFound(edge.source_id.value)
        if edge.target_id not in self._nodes:
            raise NodeNotFound(edge.target_id.value)
        self._edges[edge.edge_id] = edge
        return edge

    def get_node(self, node_id: NodeId) -> GraphNode:
        try:
            return self._nodes[node_id]
        except KeyError as exc:
            raise NodeNotFound(node_id.value) from exc

    def get_edge(self, edge_id: EdgeId) -> GraphEdge:
        try:
            return self._edges[edge_id]
        except KeyError as exc:
            raise EdgeNotFound(edge_id.value) from exc

    def remove_edge(self, edge_id: EdgeId) -> GraphEdge:
        try:
            return self._edges.pop(edge_id)
        except KeyError as exc:
            raise EdgeNotFound(edge_id.value) from exc

    def remove_node(self, node_id: NodeId, *, cascade: bool = False) -> GraphNode:
        node = self.get_node(node_id)
        connected = self.edges_for(node_id)
        if connected and not cascade:
            raise ValueError("Cannot remove a connected node without cascade=True")
        for edge in connected:
            self._edges.pop(edge.edge_id, None)
        self._nodes.pop(node_id)
        return node

    def update_node(self, node_id: NodeId, *, properties: dict | None = None) -> GraphNode:
        current = self.get_node(node_id)
        updated = replace(
            current,
            properties=dict(current.properties if properties is None else properties),
            version=current.version.next(),
        )
        self._nodes[node_id] = updated
        return updated

    def nodes(self) -> tuple[GraphNode, ...]:
        return tuple(self._nodes.values())

    def edges(self) -> tuple[GraphEdge, ...]:
        return tuple(self._edges.values())

    def edges_for(self, node_id: NodeId) -> tuple[GraphEdge, ...]:
        self.get_node(node_id)
        return tuple(
            edge for edge in self._edges.values()
            if edge.source_id == node_id or edge.target_id == node_id
        )

    def outgoing(self, node_id: NodeId) -> tuple[GraphEdge, ...]:
        self.get_node(node_id)
        return tuple(edge for edge in self._edges.values() if edge.source_id == node_id)

    def incoming(self, node_id: NodeId) -> tuple[GraphEdge, ...]:
        self.get_node(node_id)
        return tuple(edge for edge in self._edges.values() if edge.target_id == node_id)

    def neighbors(self, node_id: NodeId) -> tuple[GraphNode, ...]:
        self.get_node(node_id)
        neighbor_ids = []
        for edge in self.edges_for(node_id):
            if edge.source_id == node_id:
                neighbor_ids.append(edge.target_id)
            elif edge.target_id == node_id:
                neighbor_ids.append(edge.source_id)
        seen = set()
        result = []
        for current_id in neighbor_ids:
            if current_id not in seen:
                seen.add(current_id)
                result.append(self.get_node(current_id))
        return tuple(result)

    @property
    def node_count(self) -> int:
        return len(self._nodes)

    @property
    def edge_count(self) -> int:
        return len(self._edges)
