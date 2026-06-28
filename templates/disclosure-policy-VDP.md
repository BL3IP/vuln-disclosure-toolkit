# Vulnerability Disclosure Policy (VDP) — Template

> A publishable policy for an organization that *receives* reports. Modeled on the
> [disclose.io](https://disclose.io) core terms and CISA's VDP guidance. Replace `<ACME>`.

## Introduction
`<ACME>` values the security community. This policy describes what systems and research types
are covered, how to report vulnerabilities, and what you can expect from us.

## Safe Harbor
We will not pursue or support legal action against researchers who, in good faith, comply with
this policy. We consider activities conducted consistent with this policy to constitute
"authorized" conduct under the Computer Fraud and Abuse Act (CFAA) and similar laws, and we
waive any relevant restriction in our Terms of Service to the extent necessary to permit your
research. If legal action is initiated by a third party against you for activities conducted in
accordance with this policy, we will make this authorization known.

## Scope
**In scope**
- `*.acme.example` web applications
- The `<ACME>` mobile apps (iOS / Android)

**Out of scope**
- Denial-of-service (DoS/DDoS), volumetric or resource-exhaustion testing
- Social engineering, phishing, or physical attacks against staff or facilities
- Findings from automated scanners without a demonstrated, working exploit
- Third-party services we do not own

## Rules of Engagement
- Only interact with accounts you own or have explicit permission to test.
- Do not access, modify, or destroy data that is not yours; use test accounts/data.
- Stop and report immediately if you encounter sensitive data (PII, credentials, etc.).
- Do not publicly disclose before a coordinated date agreed with us.

## How to Report
- Email: `security@acme.example` (PGP key: `<link>`)
- Or via our program at `<HackerOne/Bugcrowd URL>`
- See our [`security.txt`](https://acme.example/.well-known/security.txt)

## Our Commitments
- We will acknowledge your report within **3 business days**.
- We will provide a triage decision and severity within **10 business days**.
- We will keep you updated on remediation progress and credit you (with consent).
- Target coordinated public disclosure: **90 days** from report, or sooner once fixed.
