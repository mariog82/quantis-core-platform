from dataclasses import dataclass, field
from typing import Any


@dataclass
class ReportTemplate:
    key: str
    title: str
    description: str = ""
    fields: list[str] = field(default_factory=list)

    def build_payload(self, data: dict[str, Any]) -> dict[str, Any]:
        if not self.fields:
            return data
        return {field: data.get(field) for field in self.fields}
