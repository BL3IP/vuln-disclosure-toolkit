# Coordinated Disclosure Timeline — Tracking Template

A living log kept by the researcher for each report. A clean timeline is itself evidence of
good-faith, professional disclosure.

| Day | Date | Event | Notes |
|-----|------|-------|-------|
| 0 | `<YYYY-MM-DD>` | Vulnerability discovered | In authorized scope |
| 0 | | Report submitted to vendor | Channel: `<security.txt / H1 / Bugcrowd>` |
| +N | | Vendor acknowledgement received | SLA target: 3 business days |
| +N | | Triage / severity confirmed | CVSS: `<vector> (<score>)` |
| +N | | CVE requested / assigned | `CVE-YYYY-NNNNN` |
| +N | | Fix developed / patch shared | Optional: validate fix |
| +N | | Fix deployed / released | Version `<x.y.z>` |
| 90 | | Coordinated public disclosure | Or earlier by mutual agreement |

## Default disclosure windows (industry norms)
- **90 days** — common default (e.g. Google Project Zero) with a 14-day grace for an
  in-progress fix.
- **CERT/CC** — 45 days default.
- Always *negotiate* the window with the vendor; extend for complex fixes, shorten if the bug
  is being actively exploited in the wild (consider faster/limited disclosure).

## Escalation if the vendor goes silent
1. Re-send via an alternate contact (security.txt, support, social).
2. Engage a coordinator: **CERT/CC** (kb.cert.org/vuls/report) or a CNA.
3. Document every attempt. Only consider public disclosure after good-faith efforts and the
   agreed window have elapsed.
