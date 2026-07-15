from core.knowledge_graph.semantic_models import SemanticMapping
from core.knowledge_graph.semantic_normalizer import SemanticNormalizer
from core.knowledge_graph.semantic_registry import SemanticRegistry


class SemanticMapper:
    def __init__(
        self,
        registry: SemanticRegistry,
        normalizer: SemanticNormalizer | None = None,
    ) -> None:
        self.registry = registry
        self.normalizer = normalizer or SemanticNormalizer()

    def map_term(self, term: str) -> SemanticMapping | None:
        normalized = self.normalizer.normalize(term)
        direct = self.registry.resolve_mapping(normalized)
        if direct is not None:
            return direct
        for concept in self.registry.concepts():
            candidates = (concept.label, concept.concept_id, *concept.aliases)
            if any(
                self.normalizer.normalize(candidate) == normalized
                for candidate in candidates
            ):
                return SemanticMapping(term, concept.concept_id, 1.0)
        return None
