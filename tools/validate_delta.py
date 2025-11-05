#!/usr/bin/env python3
import json, sys, pathlib

if __package__ in {None, ""}:
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from packages.core.validator.delta_omega_lambda import validate_delta_omega_lambda

def main():
    if len(sys.argv) < 2:
        print("Usage: validate_delta.py <path/to/delta.json>"); sys.exit(2)
    p = pathlib.Path(sys.argv[1])
    data = json.loads(p.read_text(encoding="utf-8"))
    ok, errs = validate_delta_omega_lambda(data)
    if ok:
        print("OK: ∆DΩΛ is valid")
        sys.exit(0)
    else:
        print("FAIL:")
        for e in errs: print(" -", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
