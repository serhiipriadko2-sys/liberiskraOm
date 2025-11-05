#!/usr/bin/env python3
"""Проверка синхронизации ключевых ссылок между README и docs/index.md.

Скрипт заменяет bash-реализацию, чтобы не зависеть от `rg` и специфичных
параметров `xargs`. Он читает секции "Что внутри" и "Основные разделы",
сравнивает наборы ссылок и убеждается, что файл `.nojekyll` присутствует.
Дополнительно он сканирует репозиторий на наличие неэкранированных маркеров
слияния `<<<<<<<`.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable, Sequence

ROOT_DIR = Path(__file__).resolve().parents[1]
README = ROOT_DIR / "README.md"
PORTAL = ROOT_DIR / "docs" / "index.md"
NOJEKYLL = ROOT_DIR / "docs" / ".nojekyll"

README_HEADER = "## 📌 Что внутри"
PORTAL_HEADER = "## Основные разделы"
README_DOC_PATTERN = re.compile(r"docs/[A-Za-z0-9_.\-/]+\.md")
PORTAL_DOC_PATTERN = re.compile(r"\((\d\d_[A-Za-z0-9_.\-/]+\.md)\)")
CONFLICT_LITERAL = "<" * 7 + " "


def error(message: str) -> None:
    print(f"[check_docs_sync] {message}", file=sys.stderr)


def extract_section_lines(text: str, header: str) -> list[str]:
    lines = text.splitlines()
    capturing = False
    collected: list[str] = []
    for line in lines:
        if capturing:
            if line.startswith("## "):
                break
            if not line.strip():
                break
            collected.append(line)
        elif line.strip() == header:
            capturing = True
    return collected


def extract_readme_docs(text: str) -> list[str]:
    docs: set[str] = set()
    for line in extract_section_lines(text, README_HEADER):
        docs.update(README_DOC_PATTERN.findall(line))
    return sorted(docs)


def extract_portal_docs(text: str) -> list[str]:
    docs: set[str] = set()
    for line in extract_section_lines(text, PORTAL_HEADER):
        for match in PORTAL_DOC_PATTERN.finditer(line):
            docs.add(f"docs/{match.group(1)}")
    return sorted(docs)


def ensure_files_exist(paths: Sequence[str]) -> list[str]:
    missing: list[str] = []
    for rel in paths:
        if not (ROOT_DIR / rel).is_file():
            missing.append(rel)
    return missing


def iter_repository_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        yield path


def _has_conflict_marker(line: str) -> bool:
    start = 0
    while True:
        idx = line.find(CONFLICT_LITERAL, start)
        if idx == -1:
            return False
        if idx == 0 or line[idx - 1] != "\\":
            return True
        start = idx + 1


def find_conflict_markers(paths: Iterable[Path], root: Path) -> list[str]:
    results: list[str] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            if _has_conflict_marker(line):
                rel = path.relative_to(root)
                results.append(f"{rel}:{lineno}:{line.strip()}")
    return results


def main(argv: Sequence[str] | None = None) -> int:
    _ = argv  # аргументы пока не используются
    if not README.is_file():
        error("Не найден README.md")
        return 1
    if not PORTAL.is_file():
        error("Не найден docs/index.md")
        return 1
    if not NOJEKYLL.is_file():
        error("docs/.nojekyll отсутствует — GitHub Pages не откроет файлы с подчёркиваниями")
        return 1

    readme_docs = extract_readme_docs(README.read_text(encoding="utf-8"))
    if not readme_docs:
        error("README не содержит ссылок на ключевые документы (секция 'Что внутри')")
        return 1

    portal_docs = extract_portal_docs(PORTAL.read_text(encoding="utf-8"))
    if not portal_docs:
        error("docs/index.md не содержит ссылок на основные разделы")
        return 1

    missing_in_portal = sorted(set(readme_docs) - set(portal_docs))
    missing_in_readme = sorted(set(portal_docs) - set(readme_docs))

    if missing_in_portal:
        error(
            "Ссылки из README отсутствуют на портале docs/index.md: "
            + ", ".join(missing_in_portal)
        )
        return 1
    if missing_in_readme:
        error(
            "Ссылки из docs/index.md отсутствуют в README: "
            + ", ".join(missing_in_readme)
        )
        return 1

    all_references = sorted(set(readme_docs) | set(portal_docs))
    missing_files = ensure_files_exist(all_references)
    if missing_files:
        error("Указанные файлы отсутствуют: " + ", ".join(missing_files))
        return 1

    conflicts = find_conflict_markers(iter_repository_files(ROOT_DIR), ROOT_DIR)
    if conflicts:
        error("Обнаружены нерешённые маркеры конфликта в файлах:")
        for entry in conflicts:
            error(f" - {entry}")
        return 1

    print("Документация синхронизирована: README и docs/index.md содержат одинаковые разделы.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
