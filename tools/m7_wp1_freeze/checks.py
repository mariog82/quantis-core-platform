from pathlib import Path
from core.knowledge_graph.freeze import FreezeReport, KnowledgeGraphFreezeValidator


def run_freeze_checks(root: Path | None = None) -> FreezeReport:
    return KnowledgeGraphFreezeValidator().validate(root)
