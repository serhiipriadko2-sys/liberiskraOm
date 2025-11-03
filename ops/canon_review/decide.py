#!/usr/bin/env python3
import json
from pathlib import Path

BASELINE = Path("reports/baseline_report.md")

def main() -> None:
    verdict = "keep"
    notes = []
    if not BASELINE.exists():
        verdict = "defer"
        notes.append("baseline_report.md missing")
    else:
        notes.append("baseline report present")
    payload = {
        "verdict": verdict,
        "notes": notes,
    }
    print(json.dumps(payload, ensure_ascii=False))

if __name__ == "__main__":
    main()
