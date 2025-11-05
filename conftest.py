import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

for candidate in (ROOT, *ROOT.parents):
    if (candidate / "packages").exists():
        repo_root = candidate
        break
else:
    repo_root = ROOT

repo_path = str(repo_root)
if repo_path not in sys.path:
    sys.path.insert(0, repo_path)
