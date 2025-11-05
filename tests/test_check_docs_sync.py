import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "tools"))

import check_docs_sync  # noqa: E402


def test_extractors_in_sync():
    readme = Path(check_docs_sync.README)
    portal = Path(check_docs_sync.PORTAL)
    readme_docs = check_docs_sync.extract_readme_docs(readme.read_text(encoding="utf-8"))
    portal_docs = check_docs_sync.extract_portal_docs(portal.read_text(encoding="utf-8"))
    assert readme_docs == portal_docs


def test_conflict_detection(tmp_path):
    ok = tmp_path / "escaped.txt"
    ok.write_text("\\" + "<" * 7 + " HEAD\n", encoding="utf-8")
    bad = tmp_path / "conflict.txt"
    bad.write_text("<" * 7 + " HEAD\n", encoding="utf-8")

    hits = check_docs_sync.find_conflict_markers([ok, bad], tmp_path)
    assert len(hits) == 1
    assert "conflict.txt" in hits[0]


@pytest.mark.parametrize("entry", [["unknown.md"]])
def test_missing_files(entry):
    missing = check_docs_sync.ensure_files_exist(entry)
    assert entry == missing


def test_main_success():
    assert check_docs_sync.main([]) == 0
