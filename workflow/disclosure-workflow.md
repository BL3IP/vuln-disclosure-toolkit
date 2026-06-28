# Coordinated Vulnerability Disclosure (CVD) — Workflow

A safe, repeatable, legally-aware process for finding and responsibly disclosing a vulnerability.
This repo is **documentation + tooling only**. Any actual testing must be against systems you
own or are explicitly authorized to test.

## 0. Authorization first (the most important step)
- Only test where you have permission: your own lab, an asset listed in a published VDP /
  bug-bounty scope, or a designated practice target (see below).
- Read the program's scope and rules of engagement **before** touching anything. Out-of-scope
  testing can be a crime (CFAA and equivalents) even with good intent.
- Keep DoS, social engineering, and physical attacks out unless explicitly allowed.

### Safe practice targets (intentionally vulnerable, authorized)
- **OWASP Juice Shop** — self-host (`docker run -p 3000:3000 bkimminich/juice-shop`).
- **DVWA**, **OWASP WebGoat** — self-hosted labs.
- **`testphp.vulnweb.com`** — Acunetix's public, intentionally-vulnerable test site.
- **Google XSS Game**, **PortSwigger Web Security Academy** labs.

## 1. Discover & minimize
- Find the issue using only the access your role/account legitimately has.
- Prove impact with the **least intrusive** PoC possible. Never pivot, escalate, or read other
  users' data beyond what's needed to demonstrate the bug. Stop at sensitive data and report.

## 2. Document
- Capture exact, reproducible steps, request/response, and a minimal PoC.
- Score it with CVSS v3.1 (use `tools/cvss_calculator.py`).
- Fill in [`templates/vulnerability-report-template.md`](../templates/vulnerability-report-template.md).

## 3. Find the right contact
- Check `https://<target>/.well-known/security.txt` (RFC 9116).
- Check for a VDP / bug-bounty program (HackerOne, Bugcrowd, the vendor's site).
- No channel? Use a coordinator: **CERT/CC** (kb.cert.org/vuls/report).

## 4. Report privately
- Submit through the official channel only. Encrypt if a PGP key is provided.
- Be professional and concise; offer to help validate the fix.

## 5. Coordinate
- Track everything in [`coordinated-disclosure-timeline.md`](../templates/coordinated-disclosure-timeline.md).
- Agree a disclosure window (90-day default). Request a CVE (via the vendor's CNA or MITRE).
- Be responsive and patient; extend the window for complex, good-faith fixes.

## 6. Remediation & verification
- Re-test the fix if invited. Confirm the issue is actually resolved (and not just hidden).

## 7. Public disclosure
- Disclose only after the fix ships or the agreed window elapses.
- Publish a clear write-up (root cause, impact, fix, timeline). Avoid weaponized exploits;
  give defenders detection/mitigation guidance.

## Do / Don't
| ✅ Do | ❌ Don't |
|------|---------|
| Stay in scope, use test data | Access real user data |
| Report privately first | Drop a 0-day publicly |
| Keep a clean timeline | Demand payment / threaten |
| Minimize impact | Run DoS or destructive tests |

## References
- disclose.io — https://disclose.io
- HackerOne disclosure guidelines — https://www.hackerone.com/disclosure-guidelines
- CISA CVD process — https://www.cisa.gov/coordinated-vulnerability-disclosure-process
- RFC 9116 (security.txt) — https://www.rfc-editor.org/rfc/rfc9116
- FIRST CVSS v3.1 — https://www.first.org/cvss/v3.1/specification-document
