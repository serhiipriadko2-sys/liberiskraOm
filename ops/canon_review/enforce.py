#!/usr/bin/env python3
import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("usage: enforce.py <keep|tune|amend|defer>")
        sys.exit(2)
    verdict = sys.argv[1].lower()
    allowed = {"keep", "tune", "amend", "defer"}
    if verdict not in allowed:
        print(f"invalid verdict: {verdict}")
        sys.exit(1)
    if verdict == "keep":
        print("enforce: passed (baseline stable)")
        return
    print(f"enforce: pending actions for {verdict}")

if __name__ == "__main__":
    main()
