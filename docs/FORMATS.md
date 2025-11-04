# Форматы ответов и ∆DΩΛ

Канонический хвост любого существенного ответа — ∆DΩΛ. Используйте также шаблон [`tools/DELTA_TEMPLATE.md`](../tools/DELTA_TEMPLATE.md) и валидацию [`tools/validate_delta.py`](../tools/validate_delta.py).

```json
{
  "∆": "что изменилось",
  "D": [
    {
      "source": "...",
      "inference": "...",
      "fact": true,
      "trace": "..."
    }
  ],
  "Ω": "low|medium|high",
  "Λ": "микрошаг ≤ 24ч"
}
```

### Требования
- `D` — список SIFT-блоков (`source`, `inference`, `fact ∈ {true,false,"uncertain"}`, `trace`). См. [`packages/core/memory/schemas/sift_block.schema.json`](../packages/core/memory/schemas/sift_block.schema.json).
- `Ω` оценивается на `Reflex Point` (см. [`docs/OS_SPEC_vOmega_1.2.0.md`](OS_SPEC_vOmega_1.2.0.md)).
- `Λ` — действие ≤ 24 ч; повторная проверка обязательна при невыполнении.

Примеры: [`examples/delta_ok.json`](../examples/delta_ok.json), [`examples/delta_bad.json`](../examples/delta_bad.json). Полные разъяснения и расширенные форматы находятся в [`docs/unified/FORMATS.md`](unified/FORMATS.md).
