from dataclasses import dataclass, field
from typing import Any


@dataclass
class OpenAPISpec:
    title: str
    version: str
    paths: dict[str, Any] = field(default_factory=dict)

    def add_path(self, path: str, operations: dict[str, Any]) -> None:
        self.paths[path] = operations

    def to_dict(self) -> dict[str, Any]:
        return {
            "openapi": "3.1.0",
            "info": {
                "title": self.title,
                "version": self.version,
            },
            "paths": self.paths,
        }
