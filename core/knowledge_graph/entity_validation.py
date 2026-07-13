from dataclasses import dataclass, field
from core.knowledge_graph.entities import Entity

@dataclass(frozen=True)
class EntityValidationIssue:
    code: str
    message: str

@dataclass
class EntityValidationReport:
    issues: list[EntityValidationIssue] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.issues

    def add(self, code: str, message: str) -> None:
        self.issues.append(EntityValidationIssue(code, message))

EntityValidationIssue.__test__ = False
EntityValidationReport.__test__ = False

class EntityValidator:
    def validate(self, entity: Entity) -> EntityValidationReport:
        report = EntityValidationReport()
        if not entity.entity_type.strip():
            report.add("EMPTY_ENTITY_TYPE", "Entity type must not be empty.")
        if not entity.attributes:
            report.add("EMPTY_ENTITY_ATTRIBUTES", "Entity must contain at least one attribute.")
        aliases = [alias.strip().lower() for alias in entity.aliases]
        if len(aliases) != len(set(aliases)):
            report.add("DUPLICATE_ALIAS", "Entity aliases must be unique.")
        return report
