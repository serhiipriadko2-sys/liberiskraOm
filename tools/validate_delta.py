#!/usr/bin/env python3
"""Validate ∆DΩΛ payloads stored in JSON files."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from typing import Iterable, List

if __package__ in {None, ""}:
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from packages.core.validator.delta_omega_lambda import validate_delta_omega_lambda

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_EXAMPLES = [REPO_ROOT / "examples" / "delta_ok.json"]
DELTA_GLOB = "delta*.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate one или несколько JSON-файлов с блоками ∆DΩΛ."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Файлы или директории (delta*.json), которые нужно проверить.",
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Дополнительно проверить эталонный пример из examples/.",
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Остановиться на первом найденном нарушении.",
    )
    return parser.parse_args()


def iter_directory(path: pathlib.Path) -> Iterable[pathlib.Path]:
    for candidate in sorted(path.rglob(DELTA_GLOB)):
        if candidate.is_file():
            yield candidate


def collect_targets(args: argparse.Namespace) -> List[pathlib.Path]:
    targets: List[pathlib.Path] = []
    seen: set[pathlib.Path] = set()
    missing: List[pathlib.Path] = []

    def add(path: pathlib.Path) -> None:
        real = path.resolve()
        if real not in seen:
            seen.add(real)
            targets.append(real)

    if args.examples:
        for example in DEFAULT_EXAMPLES:
            if example.exists():
                add(example)
            else:
                missing.append(example)

    for raw in args.paths:
        path = pathlib.Path(raw)
        if path.is_file():
            add(path)
        elif path.is_dir():
            found = False
            for candidate in iter_directory(path):
                add(candidate)
                found = True
            if not found:
                print(f"[WARN] {path} не содержит файлов {DELTA_GLOB}", file=sys.stderr)
        else:
            missing.append(path)

    if missing:
        lines = "\n".join(f" - {p}" for p in missing)
        print(f"[ERROR] Не удалось найти указанные пути:\n{lines}", file=sys.stderr)
        sys.exit(2)

    return targets


def format_path(path: pathlib.Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def validate_file(path: pathlib.Path) -> bool:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[FAIL] {format_path(path)} — неверный JSON: {exc}")
        return False
    except OSError as exc:
        print(f"[FAIL] {format_path(path)} — не удалось прочитать файл: {exc}")
        return False

    ok, errors = validate_delta_omega_lambda(data)
    if ok:
        print(f"[OK]   {format_path(path)}")
        return True

    print(f"[FAIL] {format_path(path)}")
    for err in errors:
        print(f"  - {err}")
    return False


def main() -> None:
    args = parse_args()
    targets = collect_targets(args)
    if not targets:
        print(
            "[ERROR] Нет файлов для проверки. Передайте путь или добавьте --examples",
            file=sys.stderr,
        )
        sys.exit(2)

    exit_code = 0
    for path in targets:
        if not validate_file(path):
            exit_code = 1
            if args.fail_fast:
                break

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
