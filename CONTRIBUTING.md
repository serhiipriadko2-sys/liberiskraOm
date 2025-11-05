# Contributing
- Все существенные ответы и PR сопровождаем ∆DΩΛ (см. examples/delta_ok.json).
- Перед отправкой изменений выполните `make check` (запускает pytest, синхронизацию документации и проверку ∆DΩΛ). При отсутствии make допустимо вручную вызвать `pytest`, `python tools/check_docs_sync.py` и `python tools/validate_delta.py --examples` или указав конкретный файл.
- Источники правды: packages/core/slo.json, packages/core/symbol_map.json, docs/OS_SPEC_vOmega_1.2.0.md.
