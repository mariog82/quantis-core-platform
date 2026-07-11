from dataclasses import dataclass


@dataclass
class BPMNMetrics:
    documents_imported: int = 0
    documents_exported: int = 0
    validation_failures: int = 0
    parse_failures: int = 0
