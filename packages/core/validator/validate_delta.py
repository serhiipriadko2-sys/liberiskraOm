import json
import sys


def _bad(msg):
    print(msg)
    return False


def validate_sift_block(block):
    need = {"source", "inference", "fact", "trace"}
    if not isinstance(block, dict):
        return False
    if not need.issubset(block):
        return False
    if not isinstance(block["source"], str) or not block["source"]:
        return False
    if block["fact"] not in [True, False, "uncertain"]:
        return False
    return True


def validate_delta_omega_lambda(delta):
    ok = True
    if "∆" not in delta or not isinstance(delta["∆"], str) or not delta["∆"]:
        ok = False
    if "Ω" not in delta or delta["Ω"] not in ["low", "medium", "high"]:
        ok = False
    if "Λ" not in delta or not isinstance(delta["Λ"], str) or not delta["Λ"]:
        ok = False
    if "D" not in delta or not isinstance(delta["D"], list):
        ok = False
    else:
        for block in delta["D"]:
            if not validate_sift_block(block):
                ok = False
                break
    return ok


if __name__ == "__main__":
    data = json.load(sys.stdin)
    print("OK" if validate_delta_omega_lambda(data) else "FAIL")
