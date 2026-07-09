from pathlib import Path


def run_test_integrity_checks(root: Path | str = "."):
    repo_root = Path(root).resolve()
    required = ["tests", "tests/sdk", "tests/framework/adapters/stabilization"]
    return [path for path in required if not (repo_root / path).exists()]
