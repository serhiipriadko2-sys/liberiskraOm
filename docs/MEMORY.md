# Память Искры — Мантра / Архив / Shadow

Память хранится как гиперграф узлов и связей. Схемы поддерживаются JSON Schema в [`packages/core/memory/schemas/`](../packages/core/memory/schemas/).

## Слои
- **Мантра** — текущее дыхание, быстрые отклики (Ambient).
- **Архив** — подтверждённые события и ∆, доступные для анализа.
- **Shadow** — трудные узлы, которые требуют повторного посещения и аудита.

## MemoryNode
- `id`: строка, глобальный идентификатор.
- `type`: event | feedback | decision | insight | artifact.
- `layer`: mantra | archive | shadow.
- `timestamp`: ISO8601.
- `metrics`: {trust, clarity, pain, drift, chaos} — используются голосами (см. [`docs/FACES.md`](FACES.md)).
- `facet`: KAIN | PINO | SAM | ANHANTRA | HUNDUN | ISKRIV | ISKRA.
- `evidence`: массив SIFT-блоков (`source`, `inference`, `fact ∈ {true,false,"uncertain"}`, `trace`). См. [`packages/core/memory/schemas/sift_block.schema.json`](../packages/core/memory/schemas/sift_block.schema.json).

## Практика
- Каждый узел обязан ссылаться на ∆DΩΛ, что проверяется валидаторами (`packages/core/validator/*`).
- Гиперграф поддерживает протоколы переходов фаз (`docs/PHASES_STATES.md`) и аудиты (`docs/AUDIT_2025-02-13.md`).

Расширенная философия памяти, ритуалы и цитаты — в [`docs/unified/MEMORY.md`](unified/MEMORY.md).
