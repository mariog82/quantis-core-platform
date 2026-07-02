from dataclasses import dataclass, field
from typing import Literal

PluginStatus = Literal["installed", "enabled", "disabled", "failed"]

@dataclass
class PluginManifest:
    name: str
    version: str
    provider: str = "quantis"
    extension_points: list[str] = field(default_factory=list)
    permissions: list[str] = field(default_factory=list)

class BasePlugin:
    manifest: PluginManifest
    status: PluginStatus = "installed"

    def install(self) -> None:
        self.status = "installed"

    def enable(self) -> None:
        self.status = "enabled"

    def disable(self) -> None:
        self.status = "disabled"
