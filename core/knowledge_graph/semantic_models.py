from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class SemanticConcept:
    concept_id: str
    label: str
    parent_ids: tuple[str, ...] = ()
    aliases: tuple[str, ...] = ()
    properties: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.concept_id.strip():
            raise ValueError("concept_id must not be empty")
        if not self.label.strip():
            raise ValueError("label must not be empty")


@dataclass(frozen=True)
class SemanticProperty:
    property_id: str
    label: str
    value_type: str = "string"
    aliases: tuple[str, ...] = ()


@dataclass(frozen=True)
class SemanticRelationship:
    relationship_id: str
    label: str
    source_concept_id: str
    target_concept_id: str
    inverse_id: str | None = None
    transitive: bool = False
    symmetric: bool = False


@dataclass(frozen=True)
class SemanticMapping:
    source_term: str
    target_concept_id: str
    confidence: float = 1.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")


@dataclass(frozen=True)
class SemanticInference:
    subject_id: str
    predicate: str
    object_id: str
    reason: str
