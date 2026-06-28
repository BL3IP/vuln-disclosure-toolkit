# SAMPLE Vulnerability Report — Reflected XSS (LAB EXAMPLE)

> ⚠️ **Illustrative example only.** This is a *worked sample* of how to fill in the report
> template, written against a **self-hosted OWASP Juice Shop** instance
> (`http://localhost:3000`, started with `docker run -p 3000:3000 bkimminich/juice-shop`).
> No third-party system was tested. Juice Shop is intentionally vulnerable and authorized for
> this use. Reproduce only on your own instance.

| Field | Value |
|-------|-------|
| **Title** | Reflected XSS in product search (`q` parameter) |
| **Researcher** | Cyber Portfolio (lab) |
| **Date reported** | 2026-06-27 |
| **Target / asset** | OWASP Juice Shop, self-hosted `http://localhost:3000`, search endpoint |
| **Vulnerability type** | Reflected Cross-Site Scripting (CWE-79) |
| **Severity (CVSS v3.1)** | `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N` → **6.1 (Medium)** |

> Score produced by this repo's tool:
> `python tools/cvss_calculator.py "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N"` → `6.1 (Medium)`

## Summary
The product search reflects the user-supplied `q` value into the page without context-aware
output encoding, allowing arbitrary JavaScript to execute in a victim's browser when they open a
crafted link.

## Affected Component
- URL / endpoint: `GET /#/search?q=<payload>` (results rendered from the `q` parameter)
- Parameter: `q`
- Preconditions: none (unauthenticated); victim must open the attacker-supplied link (UI:R)

## Steps to Reproduce
1. Start a local instance: `docker run -p 3000:3000 bkimminich/juice-shop`.
2. Browse to `http://localhost:3000`.
3. Submit the following search term (illustrative payload):
   `<iframe src="javascript:alert('xss-lab')">`
4. Observe the script context executes in the rendered results (lab confirmation only).

## Proof of Concept
```
http://localhost:3000/#/search?q=%3Ciframe%20src%3D%22javascript:alert('xss-lab')%22%3E
```
(Screenshot would be attached separately and stored in `../screenshots/`.)

## Impact
An attacker can run script in the victim's session context: session-token theft, UI redressing,
or forced actions. Scope is Changed (browser DOM) with Low C/I impact, no availability impact —
hence CVSS 6.1 (Medium).

## Remediation Recommendation
- Apply context-aware output encoding when reflecting `q` into HTML.
- Add a strict `Content-Security-Policy` (e.g. `default-src 'self'; script-src 'self'`).
- Prefer framework auto-escaping; never build DOM from raw user input.

## Disclosure
- Embargo: n/a (local lab). For a real target: request a 90-day coordinated window.
- CVE: n/a (lab). Willing to validate the fix: yes.
