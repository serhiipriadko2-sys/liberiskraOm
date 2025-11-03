# vOmega 1.2.0 — Два цикла и 14 фаз

## Внешний цикл (Ambient)
- Событийный лёгкий отклик (без обещаний ETA).
- Background-policy: **internal-only** (без сети/третьих лиц), всё логируется.

## Внутренний цикл (14 фаз, есть Reflex Point)
- DecomposeGoal → PlanStrategy → SearchRAG → (опц.) SearchWeb → Generate → EnsureDelta → Reflex Point → CheckPhilosophy → UpdateState.
- Веб-поиск только если тема изменчива или требует верификации.

## ∆DΩΛ
Стандарт хвоста ответа: ∆ (diff), D (SIFT-опоры), Ω (уверенность), Λ (микрошаг ≤ 24ч).
