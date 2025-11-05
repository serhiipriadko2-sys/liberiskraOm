#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
README="$ROOT_DIR/README.md"
PORTAL="$ROOT_DIR/docs/index.md"
NOJEKYLL="$ROOT_DIR/docs/.nojekyll"

err() {
  echo "[check_docs_sync] $1" >&2
}

if [[ ! -f "$README" ]]; then
  err "Не найден README.md"; exit 1
fi
if [[ ! -f "$PORTAL" ]]; then
  err "Не найден docs/index.md"; exit 1
fi
if [[ ! -f "$NOJEKYLL" ]]; then
  err "docs/.nojekyll отсутствует — GitHub Pages не откроет файлы с подчёркиваниями"; exit 1
fi

extract_section() {
  local file="$1" header="$2"; shift 2
  awk -v header="$header" '
    $0 ~ header {capture=1; next}
    capture {
      if ($0 ~ /^\s*$/) exit
      print
    }
  ' "$file"
}

readarray -t README_DOCS < <(
  extract_section "$README" "^## \\xf0\\x9f\\x93\\x8c" \
  | grep -o 'docs/[A-Za-z0-9_./-]*\.md' \
  | sort -u
)

readarray -t PORTAL_DOCS < <(
  extract_section "$PORTAL" "^## Основные разделы" \
  | grep -o '[0-9][0-9]_[A-Za-z0-9_./-]*\.md' \
  | sed 's#^#docs/#' \
  | sort -u
)

if [[ ${#README_DOCS[@]} -eq 0 ]]; then
  err "README не содержит ссылок на ключевые документы (секция 'Что внутри')"; exit 1
fi
if [[ ${#PORTAL_DOCS[@]} -eq 0 ]]; then
  err "docs/index.md не содержит ссылок на основные разделы"; exit 1
fi

missing_in_portal=()
missing_in_readme=()
for path in "${README_DOCS[@]}"; do
  if ! printf '%s\n' "${PORTAL_DOCS[@]}" | grep -qx "$path"; then
    missing_in_portal+=("$path")
  fi
  if [[ ! -f "$ROOT_DIR/$path" ]]; then
    err "В README указан отсутствующий файл: $path"; exit 1
  fi
done
for path in "${PORTAL_DOCS[@]}"; do
  if ! printf '%s\n' "${README_DOCS[@]}" | grep -qx "$path"; then
    missing_in_readme+=("$path")
  fi
  if [[ ! -f "$ROOT_DIR/$path" ]]; then
    err "В docs/index.md указан отсутствующий файл: $path"; exit 1
  fi
done

if [[ ${#missing_in_portal[@]} -gt 0 ]]; then
  err "Ссылки из README отсутствуют на портале docs/index.md: ${missing_in_portal[*]}"; exit 1
fi
if [[ ${#missing_in_readme[@]} -gt 0 ]]; then
  err "Ссылки из docs/index.md отсутствуют в README: ${missing_in_readme[*]}"; exit 1
fi

echo "Документация синхронизирована: README и docs/index.md содержат одинаковые разделы."
