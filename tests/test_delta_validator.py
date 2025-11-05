import json
import pathlib
import subprocess
import sys

from packages.core.validator.delta_omega_lambda import validate_delta_omega_lambda

def load(p): return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def test_ok():
    ok, errs = validate_delta_omega_lambda(load("examples/delta_ok.json"))
    assert ok and not errs

def test_bad():
    ok, errs = validate_delta_omega_lambda(load("examples/delta_bad.json"))
    assert not ok
    assert any("∆ is missing" in e for e in errs)


def _run_cli(args, input_text=None):
    result = subprocess.run(
        [sys.executable, "-m", "packages.core.validator.validate_delta", *args],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    return result


def test_cli_accepts_path():
    result = _run_cli(["examples/delta_ok.json"])
    assert result.returncode == 0
    assert "OK" in result.stdout
    assert not result.stderr


def test_cli_accepts_stdin():
    payload = json.dumps(load("examples/delta_bad.json"))
    result = _run_cli([], input_text=payload)
    assert result.returncode == 1
    assert "FAIL" in result.stdout
    assert "∆ is missing" in result.stdout
