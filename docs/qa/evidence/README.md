# Test Evidence — Guide

## Naming standard
- Test‑case screenshots: `SS-YYYY-MM-DD-TC###-short-description.png`
  - Example: `SS-2025-10-08-TC001-registration-valid.png`
- “Meta” artifacts (not tied to a single TC): `SS-YYYY-MM-DD-meta-short-description.png`
  - Examples: `SS-2025-10-08-meta-landing.png`, `SS-2025-10-08-network-clean.png`, `SS-2025-10-08-console-clean.png`

Notes:
- Use three digits for test case numbers (TC001, TC010).
- Use short, kebab‑case descriptions (registration, login, symptoms, results, pdf, mobile‑view).

## What to capture
- Key pages: registration, login, symptoms form, results, PDF
- Error/validation messages (if any)
- Mobile viewport (one screenshot, e.g., iPhone 12 via Chrome DevTools)
- DevTools Console with any visible error (or a “clean” console if relevant)
- Network tab (clean 200 OK or failing requests if any)

## Where
- This folder `qa/evidence` stores all evidence referenced by test cases and issues.

## Tips
- Use Incognito and disable cache while DevTools is open.
- Console: enable “Preserve log” and refresh before capturing.
- Mobile: Device toolbar at 100% zoom; iPhone 12 preset.
- Prefer PNG. Avoid including any sensitive personal data in screenshots.
