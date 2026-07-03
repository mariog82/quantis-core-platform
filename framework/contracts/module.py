from dataclasses import dataclass, field
from typing import Literal


ModuleStatus = Literal["draft", "active", "deprecated", "disabled"]


@dataclass
class ModuleManifest:
    name: str
    version: str
    description: str = ""
    capabilities: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    status: ModuleStatus = "draft"


class BaseModule:
    manifest: ModuleManifest

    def boot(self) -> None:
        raise NotImplementedError

    def shutdown(self) -> None:
        raise NotImplementedError

    def health(self) -> dict:
        return {
            "name": self.manifest.name,
            "version": self.manifest.version,
            "status": self.manifest.status,
        }