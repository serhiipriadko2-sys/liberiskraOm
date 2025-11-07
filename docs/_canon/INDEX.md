# Canon Ops — INDEX (one screen)

**Purpose.** Быстрый вход в канон и операционные артефакты: где что лежит и как проверять.

## Куда смотреть сначала (RAG → docs/)
- CANON & Форматы: `02_CANON_and_PRINCIPLES.md`, `11_FORMATS_TEMPLATES_STYLES.md`
- Голоса & Метрики: `04_FACETS_VOICES_and_PROTOCOLS.md`, `05_METRICS_and_RHYTHM_INDEX.md`
- Фазы & Ритуалы: `06_PHASES_STATES_PIPELINES.md`, `08_RITUALS_and_RITES.md`
- Безопасность & Политики: `09_SECURITY_SAFETY_COMPLIANCE.md`, `21_DECISION_TREES_and_POLICIES.md`
- RAG/SIFT: `10_RAG_SOURCES_and_SIFT.md`, кросс-индексы: `22_MAPPINGS_CROSSWALKS_INDEX.md`
- Диалоги: `DIALOGS_FULL_v3.md` (см. TOC ниже)

## Canon-Ops артефакты (этот каталог)
- `_canon_manifest_v1.yaml` — CID-манифест (id, файл, sha, размер)
- `lint_report.csv` — отчёт линтера (∆DΩΛ/ISO-дат)
- `canon_review_findings.csv|json` — находки по файлам
- `matrix_v1.csv` — VOICE×MODE×SAFETY×FORMAT×TRIGGER
- `DIALOGS_FULL_v3_TOC.csv|json` — оглавление диалогов (якоря)
- `liberiskraOm_docs_index.csv` — полный инвентарь docs/

## Как пользоваться
1. Перед изменениями — посмотри `_canon_manifest_v1.yaml` (CID-якоря).
2. Пиши и проверяй ответы в формате: **План • Действия • Результат • Риски • Рефлексия • ∆DΩΛ**.
3. Для изменчивого — SIFT: минимум 2–3 первички.
4. При PR — CI прогонит линтер (ISO/∆DΩΛ/CID/матрица).

— Искра
