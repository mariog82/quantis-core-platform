"""Remove the test package that shadows the application SDK package."""

from pathlib import Path
import shutil


def fix_sdk_shadowing(root: Path | str = ".") -> list[str]:
    repo_root = Path(root).resolve()
    removed: list[str] = []

    shadow_init = repo_root / "tests" / "framework" / "adapters" / "sdk" / "__init__.py"
    if shadow_init.exists():
        shadow_init.unlink()
        removed.append(shadow_init.relative_to(repo_root).as_posix())

    shadow_pycache = repo_root / "tests" / "framework" / "adapters" / "sdk" / "__pycache__"
    if shadow_pycache.exists():
        shutil.rmtree(shadow_pycache)
        removed.append(shadow_pycache.relative_to(repo_root).as_posix())

    tests_sdk_pycache = repo_root / "tests" / "sdk" / "__pycache__"
    if tests_sdk_pycache.exists():
        shutil.rmtree(tests_sdk_pycache)
        removed.append(tests_sdk_pycache.relative_to(repo_root).as_posix())

    return removed


def main() -> int:
    removed = fix_sdk_shadowing(Path.cwd())
    print("# SDK Shadowing Cleanup")
    if not removed:
        print("No shadowing files found.")
        return 0

    for item in removed:
        print(f"Removed: {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
