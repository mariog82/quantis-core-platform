from pathlib import Path
import re


def run_release_manager_checks(root: Path | str = "."):
    repo_root = Path(root).resolve()
    version_file = repo_root / "VERSION"
    if not version_file.exists():
        return ["missing VERSION"]
    version = version_file.read_text(encoding="utf-8").strip()
    if not re.match(r"^\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?$", version):
        return [f"invalid VERSION {version}"]
    release_doc = repo_root / "docs/release/M5_1_BETA_FREEZE.md"
    if version == "0.5.1-beta.1" and not release_doc.exists():
        return ["missing docs/release/M5_1_BETA_FREEZE.md"]
    return []
