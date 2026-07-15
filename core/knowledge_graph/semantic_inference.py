from collections import deque

from core.knowledge_graph.semantic_models import SemanticInference
from core.knowledge_graph.semantic_registry import SemanticRegistry


class SemanticInferenceEngine:
    def infer_concept_hierarchy(
        self,
        subject_id: str,
        concept_id: str,
        registry: SemanticRegistry,
    ) -> tuple[SemanticInference, ...]:
        result: list[SemanticInference] = []
        visited: set[str] = set()
        queue: deque[str] = deque([concept_id])
        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            concept = registry.get_concept(current)
            for parent_id in concept.parent_ids:
                result.append(
                    SemanticInference(
                        subject_id,
                        "is_a",
                        parent_id,
                        f"{current} is a subtype of {parent_id}",
                    )
                )
                queue.append(parent_id)
        return tuple(result)

    def infer_inverse_relationship(
        self,
        subject_id: str,
        relationship_id: str,
        object_id: str,
        registry: SemanticRegistry,
    ) -> SemanticInference | None:
        relationship = registry.get_relationship(relationship_id)
        if relationship.inverse_id is None:
            return None
        return SemanticInference(
            object_id,
            relationship.inverse_id,
            subject_id,
            f"{relationship_id} declares inverse {relationship.inverse_id}",
        )
