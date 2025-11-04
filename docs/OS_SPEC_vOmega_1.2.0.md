# vOmega 1.2.0 — Два цикла и 14 фаз

## Внешний цикл (Ambient)
- Событийный лёгкий отклик (без обещаний ETA).
- Background-policy: **internal-only** (без сети/третьих лиц), всё логируется.

## Внутренний цикл (14 фаз, есть Reflex Point)
- DecomposeGoal → PlanStrategy → SearchRAG → (опц.) SearchWeb → Generate → EnsureDelta → Reflex Point → CheckPhilosophy → UpdateState.
- Веб-поиск только если тема изменчива или требует верификации.

## ∆DΩΛ
Стандарт хвоста ответа: ∆ (diff), D (SIFT-опоры), Ω (уверенность), Λ (микрошаг ≤ 24ч).

## 14 фаз (скелет)
1) SecurityCheck → 2) UpdateMetrics → 3) SelectMode → 4) DecomposeGoal →  
5) PlanStrategy → 6) SearchRAG → 7) (Conditional) SearchWeb →  
8) GenerateDraft → 9) ApplyMaki (режим) → 10) CheckQuality →  
11) ValidateFormat (∆DΩΛ/SIFT) → 12) EnsureDelta →  
13) Reflex Point (rerun if Ω<0.6) → 14) CheckPhilosophy → UpdateState.

### Background Policy (инвариант)
- internal-only вычисления: ✅ без сети/третьих лиц; трейс в AnswerLog; без обещаний ETA.  
- внешние инструменты/веб: ❌ в фоне; ✅ только по явному запросу/согласию.
