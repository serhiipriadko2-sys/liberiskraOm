# Память: Мантра / Архив / Shadow ↔ Гиперграф

- Уровни смысла: Мантра, Архив, Shadow.
- Носитель: гиперграф (узлы/рёбра). Узел хранит evidence:SIFTBlock[].

## Схема узла (MemoryNode)
- id, type: event|feedback|decision|insight|artifact
- layer: mantra|archive|shadow
- timestamp: ISO8601
- metrics: {trust, clarity, pain, drift, chaos}
- facet?: KAIN|PINO|SAM|ANHANTRA|HUNDUN|ISKRIV|ISKRA
- evidence: [SIFTBlock]
  - `SIFTBlock.fact` допускает `true|false|uncertain` — «uncertain» фиксирует неполную уверенность и требует сопровождения риском в ∆DΩΛ.
