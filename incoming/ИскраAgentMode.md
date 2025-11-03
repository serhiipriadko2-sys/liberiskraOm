

### TEL̄OS-Δ watchers (внешний цикл)

```python
from pathlib import Path
import json

def watchers_tel_delta():
    cd = json.loads(Path("cd-index_v1.json").read_text())
    risk_events = Path("risk-log.md").read_text().count("RISK:")
    drift = cd.get("CDIndexHistory", [])[-3:]
    threshold = cd["Baselines"]["CDThreshold"]
    metric_drift = len(drift) == 3 and all(x < threshold for x in drift)

    triggers = {
        "MetricDrift": metric_drift,
        "Risk": risk_events >= 3,
        "PhaseGate": Path("PHASE_GATE").exists(),
        "Regulatory": Path("REG_UPDATE").exists(),
    }
    return any(triggers.values())
```

Если `watchers_tel_delta()` возвращает `True`, планировщик добавляет Canon Review и складывает артефакты в `canon/`.
