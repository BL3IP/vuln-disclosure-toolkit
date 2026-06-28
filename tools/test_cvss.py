"""Validate the CVSS v3.1 calculator against official, published vectors/scores."""
import pytest

from cvss_calculator import score_vector

# (vector, expected base score, expected severity) — values from first.org/cvss
CASES = [
    ("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", 9.8, "Critical"),  # full RCE
    ("CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N", 6.1, "Medium"),    # reflected XSS
    ("CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H", 7.8, "High"),      # local priv-esc
    ("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H", 7.5, "High"),      # network DoS
    ("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:N", 0.0, "None"),      # no impact
]


@pytest.mark.parametrize("vector,expected_score,expected_sev", CASES)
def test_official_vectors(vector, expected_score, expected_sev):
    score, sev = score_vector(vector)
    assert score == expected_score
    assert sev == expected_sev


def test_missing_metric_raises():
    with pytest.raises(ValueError):
        score_vector("CVSS:3.1/AV:N/AC:L")
