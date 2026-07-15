from copy import deepcopy
from core.knowledge_graph.graph import KnowledgeGraph
from core.knowledge_graph.identifiers import NodeId
from core.knowledge_graph.repository import GraphRepository, GraphSnapshot
from core.knowledge_graph.serialization import JsonGraphSerializer

class InMemoryGraphRepository(GraphRepository):
    def __init__(self) -> None:
        self._graphs: dict[str, KnowledgeGraph] = {}
        self._revisions: dict[str, int] = {}
        self._serializer = JsonGraphSerializer()

    def save(self, graph_id: str, graph: KnowledgeGraph) -> KnowledgeGraph:
        if not graph_id.strip():
            raise ValueError("graph_id must not be empty")
        stored = deepcopy(graph)
        self._graphs[graph_id] = stored
        self._revisions[graph_id] = self._revisions.get(graph_id, 0) + 1
        return deepcopy(stored)

    def get(self, graph_id: str) -> KnowledgeGraph | None:
        graph = self._graphs.get(graph_id)
        return deepcopy(graph) if graph is not None else None

    def delete(self, graph_id: str) -> KnowledgeGraph:
        try:
            graph = self._graphs.pop(graph_id)
        except KeyError as exc:
            raise KeyError(graph_id) from exc
        self._revisions.pop(graph_id, None)
        return deepcopy(graph)

    def exists(self, graph_id: str) -> bool:
        return graph_id in self._graphs

    def list_ids(self) -> list[str]:
        return sorted(self._graphs)

    def snapshot(self, graph_id: str) -> GraphSnapshot:
        graph = self.get(graph_id)
        if graph is None:
            raise KeyError(graph_id)
        return GraphSnapshot(
            graph_id=graph_id,
            revision=self._revisions[graph_id],
            payload=self._serializer.serialize(graph),
        )

    def restore(self, snapshot: GraphSnapshot) -> KnowledgeGraph:
        graph = self._serializer.deserialize(snapshot.payload)
        self._graphs[snapshot.graph_id] = deepcopy(graph)
        self._revisions[snapshot.graph_id] = snapshot.revision
        return deepcopy(graph)

    def find_node(self, graph_id: str, node_id: NodeId):
        graph = self.get(graph_id)
        if graph is None:
            raise KeyError(graph_id)
        return graph.get_node(node_id)
