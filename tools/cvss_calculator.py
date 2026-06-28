"""CVSS v3.1 Base Score calculator — zero dependencies.

Implements the official CVSS v3.1 base-score equations and roundup function
(https://www.first.org/cvss/v3.1/specification-document). Useful when triaging
a vulnerability for a disclosure report.

Usage:
    python cvss_calculator.py "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
"""
from __future__ import annotations

import math
import sys

WEIGHTS = {
    "AV": {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2},
    "AC": {"L": 0.77, "H": 0.44},
    "UI": {"N": 0.85, "R": 0.62},
    "C": {"H": 0.56, "L": 0.22, "N": 0.0},
    "I": {"H": 0.56, "L": 0.22, "N": 0.0},
    "A": {"H": 0.56, "L": 0.22, "N": 0.0},
}
# Privileges Required is weighted differently when Scope is Changed
PR_UNCHANGED = {"N": 0.85, "L": 0.62, "H": 0.27}
PR_CHANGED = {"N": 0.85, "L": 0.68, "H": 0.50}

REQUIRED = ("AV", "AC", "PR", "UI", "S", "C", "I", "A")


def roundup(value: float) -> float:
    """Official CVSS v3.1 roundup (avoids floating-point rounding errors)."""
    int_input = round(value * 100000)
    if int_input % 10000 == 0:
        return int_input / 100000.0
    return (math.floor(int_input / 10000) + 1) / 10.0


def parse_vector(vector: str) -> dict:
    metrics = {}
    for part in vector.strip().split("/"):
        if ":" in part:
            key, val = part.split(":", 1)
            metrics[key] = val
    return metrics


def base_score(m: dict) -> float:
    scope_changed = m["S"] == "C"
    pr = (PR_CHANGED if scope_changed else PR_UNCHANGED)[m["PR"]]

    iss = 1 - (
        (1 - WEIGHTS["C"][m["C"]])
        * (1 - WEIGHTS["I"][m["I"]])
        * (1 - WEIGHTS["A"][m["A"]])
    )
    if scope_changed:
        impact = 7.52 * (iss - 0.029) - 3.25 * ((iss - 0.02) ** 15)
    else:
        impact = 6.42 * iss

    exploitability = (
        8.22
        * WEIGHTS["AV"][m["AV"]]
        * WEIGHTS["AC"][m["AC"]]
        * pr
        * WEIGHTS["UI"][m["UI"]]
    )

    if impact <= 0:
        return 0.0
    raw = impact + exploitability
    if scope_changed:
        raw *= 1.08
    return roundup(min(raw, 10.0))


def severity(score: float) -> str:
    if score == 0.0:
        return "None"
    if score < 4.0:
        return "Low"
    if score < 7.0:
        return "Medium"
    if score < 9.0:
        return "High"
    return "Critical"


def score_vector(vector: str):
    """Return (base_score, severity) for a CVSS v3.1 vector string."""
    metrics = parse_vector(vector)
    missing = [k for k in REQUIRED if k not in metrics]
    if missing:
        raise ValueError("missing base metrics: " + ", ".join(missing))
    s = base_score(metrics)
    return s, severity(s)


def main(argv=None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print(__doc__)
        return 2
    score, sev = score_vector(argv[0])
    print(f"{argv[0]}\n  Base Score: {score}  ({sev})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
