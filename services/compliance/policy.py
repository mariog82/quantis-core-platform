from dataclasses import dataclass, field


@dataclass
class CompliancePolicy:
    key: str
    name: str
    required_controls: list[str] = field(default_factory=list)
