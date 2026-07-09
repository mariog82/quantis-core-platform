from pathlib import Path
from tools.repository_recovery import find_pycache_only_directories, remove_pycache_only_directories

def test_repository_recovery_removes_pycache_only(tmp_path: Path):
    target = tmp_path / "tests/sdk"
    target.mkdir(parents=True)
    (target / "__pycache__").mkdir()
    assert find_pycache_only_directories(tmp_path)
    result = remove_pycache_only_directories(tmp_path)
    assert result.count == 1
    assert not target.exists()
