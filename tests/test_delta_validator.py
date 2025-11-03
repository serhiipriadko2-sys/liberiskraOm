import json, pathlib
from packages.core.validator.delta_omega_lambda import validate_delta_omega_lambda

def load(p): return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def test_ok():
    ok, errs = validate_delta_omega_lambda(load("examples/delta_ok.json"))
    assert ok and not errs

def test_bad():
    ok, errs = validate_delta_omega_lambda(load("examples/delta_bad.json"))
    assert not ok
    assert any("∆ is missing" in e for e in errs)
