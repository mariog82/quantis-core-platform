from dataclasses import dataclass, field

from core.knowledge_graph.semantic_models import SemanticConcept, SemanticRelationship
from core.knowledge_graph.semantic_registry import SemanticRegistry


@dataclass(frozen=True)
class SemanticValidationIssue:
    code: str
    message: str


@dataclass
class SemanticValidationReport:
    issues: list[SemanticValidationIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def add(self, code: str, message: str) -> None:
        self.issues.append(SemanticValidationIssue(code, message))


class SemanticValidator:
    def validate_concept(
        self,
        concept: SemanticConcept,
        registry: SemanticRegistry,
    ) -> SemanticValidationReport:
        report = SemanticValidationReport()
        for parent_id in concept.parent_ids:
            try:
                registry.get_concept(parent_id)
            except KeyError:
                report.add("UNKNOWN_PARENT", f"Unknown parent concept: {parent_id}")
        return report

    def validate_relationship(
        self,
        relationship: SemanticRelationship,
        registry: SemanticRegistry,
    ) -> SemanticValidationReport:
        report = SemanticValidationReport()
        for concept_id, code in (
            (relationship.source_concept_id, "UNKNOWN_SOURCE_CONCEPT"),
            (relationship.target_concept_id, "UNKNOWN_TARGET_CONCEPT"),
        ):
            try:
                registry.get_concept(concept_id)
            except KeyError:
                report.add(code, f"Unknown concept: {concept_id}")
        if relationship.inverse_id is not None:
            try:
                registry.get_relationship(relationship.inverse_id)
            except KeyError:
                report.add(
                    "UNKNOWN_INVERSE_RELATIONSHIP",
                    f"Unknown inverse relationship: {relationship.inverse_id}",
                )
        return report
