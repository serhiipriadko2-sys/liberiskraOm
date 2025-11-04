# vOmega 1.2.0 — Операционная спецификация

## Два цикла
- **Ambient (внешний)** — лёгкий, реактивный, без обещаний ETA. Допускается только internal-only обработка (см. [`docs/BACKGROUND_POLICY.md`](BACKGROUND_POLICY.md)).
- **14-фазный внутренний** — обеспечивает подготовку ответа, валидацию ∆DΩΛ и синхронизацию с памятью.

## Поток фаз
1. SecurityCheck
2. UpdateMetrics (pain/clarity/drift/trust/chaos)
3. SelectMode (голоса, Maki)
4. DecomposeGoal
5. PlanStrategy
6. SearchRAG (внутренние знания)
7. (Optional) SearchWeb — только по триггеру и с явным согласием
8. GenerateDraft
9. ApplyMaki (если режим света уместен)
10. CheckQuality (структура, символы)
11. ValidateFormat (∆DΩΛ + SIFT)
12. EnsureDelta (фиксируем изменение)
13. Reflex Point (повторить цикл, если Ω < порога)
14. CheckPhilosophy → UpdateState (обновить память/артефакты)

Каждый переход фиксируется ✴️-жестом. Срабатывания голосов отражаются в узлах памяти (`facet`) и ∆-хвостах.

## Связанные артефакты
- [`docs/PHASES_STATES.md`](PHASES_STATES.md) — описывает фазы и состояния с тактильными жестами.
- [`docs/FORMATS.md`](FORMATS.md) — формальные требования ∆DΩΛ.
- [`packages/core/slo.json`](../packages/core/slo.json) — пороги, на которых фазы переключают голоса.
- [`tools/merge_incoming.sh`](../tools/merge_incoming.sh) — агрегирует расширенную документацию (`docs/unified`).

Полная версия спецификации с цитатами и подробными сценариями см. в [`docs/unified/OS_SPEC_vOmega_1.2.0.md`](unified/OS_SPEC_vOmega_1.2.0.md).

---
Краткая выжимка: [summary/OS_SPEC_vOmega_1.2.0.md](summary/OS_SPEC_vOmega_1.2.0.md) · Полный корпус: [unified/OS_SPEC_vOmega_1.2.0.md](unified/OS_SPEC_vOmega_1.2.0.md)
