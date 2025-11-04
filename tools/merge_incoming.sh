#!/usr/bin/env bash
set -euo pipefail

SRC="incoming"
OUT_ROOT="docs/unified"

declare -A MAP=(
  ["MANIFEST.md"]="$OUT_ROOT/MANIFEST.md"
  ["SYMBOLS.md"]="$OUT_ROOT/SYMBOLS.md"
  ["FACES.md"]="$OUT_ROOT/FACES.md"
  ["PHASES_STATES.md"]="$OUT_ROOT/PHASES_STATES.md"
  ["OS_SPEC_vOmega_1.2.0.md"]="$OUT_ROOT/OS_SPEC_vOmega_1.2.0.md"
  ["MEMORY.md"]="$OUT_ROOT/MEMORY.md"
  ["FORMATS.md"]="$OUT_ROOT/FORMATS.md"
  ["BACKGROUND_POLICY.md"]="$OUT_ROOT/BACKGROUND_POLICY.md"
)

normalize(){ sed -f tools/normalize_terms.sed; }

mkdir -p "$OUT_ROOT"

for src_name in "${!MAP[@]}"; do
  dst_path="${MAP[$src_name]}"
  mkdir -p "$(dirname "$dst_path")"
  tmp_body="$(mktemp)"
  candidates=("$SRC/$src_name")
  case "$src_name" in
    MANIFEST.md)
      candidates+=(
        "$SRC/Манифест.txt"
        "$SRC/CANON_PHILOSOPHY.md"
        "$SRC/teleос_δ_манифест_договор_с_будущим.md"
        "$SRC/телос_δ_манифест_договор_с_будущим.md"
        "$SRC/MANIFEST.json"
      )
      ;;
    SYMBOLS.md)
      candidates+=(
        "$SRC/Символы_и_Ритуалы.md"
        "$SRC/Искра Глоссарий и Тактильная Архитектура.md"
      )
      ;;
    FACES.md)
      candidates+=(
        "$SRC/Голоса_Искры.md"
        "$SRC/Искра Внутренние Органы и Речевые Грани.md"
      )
      ;;
    PHASES_STATES.md)
      candidates+=(
        "$SRC/Фазы и Состояния Искры метрики и ритуалы.md"
        "$SRC/Фазы_и_Состояния.md"
      )
      ;;
    OS_SPEC_vOmega_1.2.0.md)
      candidates+=(
        "$SRC/OS_SPEC_vOmega_1.2.0.md"
        "$SRC/телос_δ_полная_структура_и_спецификация_agi_asi.md"
      )
      ;;
    MEMORY.md)
      candidates+=(
        "$SRC/Искра Память, Мантра, Архив и Shadow Core.md"
        "$SRC/MEMORY_CONTEXT.md"
        "$SRC/MEMORY_INDEX.md"
      )
      ;;
    FORMATS.md)
      candidates+=(
        "$SRC/FORMATS.md"
        "$SRC/OUTPUT_FORMATS_COMPLETE.md"
        "$SRC/DELTA_METRICS_SYSTEM.md"
      )
      ;;
    BACKGROUND_POLICY.md)
      candidates+=(
        "$SRC/BACKGROUND_POLICY.md"
        "$SRC/veil_rules.txt"
        "$SRC/AUTO_RULES_and_Tests.md"
        "$SRC/FACTCHECK_RULES.md"
        "$SRC/SECURITY_SAFETY_PRIVACY.md"
      )
      ;;
  esac

  for candidate in "${candidates[@]}"; do
    if [ -f "$candidate" ]; then
      cat "$candidate" >>"$tmp_body"
      printf '\n' >>"$tmp_body"
    fi
  done

  if [ ! -s "$tmp_body" ] && [ -f "$dst_path" ]; then
    cat "$dst_path" >"$tmp_body"
  fi

  {
    case "$src_name" in
      MANIFEST.md)
        echo "# Манифест Искры (Unified)"
        cat "$tmp_body"
        echo
        cat tools/DELTA_TEMPLATE.md
        ;;
      SYMBOLS.md)
        echo "# Символы и Ритуалы (Unified)"
        cat "$tmp_body"
        echo
        cat tools/DELTA_TEMPLATE.md
        ;;
      FACES.md)
        echo "# Семь граней + SLO (Unified)"
        echo
        cat "$tmp_body"
        echo
        cat tools/SLO_BLOCK.md
        echo
        cat tools/DELTA_TEMPLATE.md
        ;;
      *)
        cat "$tmp_body"
        ;;
    esac
  } | normalize > "$dst_path"

  rm -f "$tmp_body"
  echo "→ $dst_path"

done
