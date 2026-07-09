from pathlib import Path


def run_repository_audit(root: Path | str = "."):
    repo_root = Path(root).resolve()
    files = [p for p in repo_root.rglob("*") if p.is_file() and ".git" not in p.parts]
    py_files = [p for p in files if p.suffix == ".py"]
    return {"files": len(files), "python_files": len(py_files)}
