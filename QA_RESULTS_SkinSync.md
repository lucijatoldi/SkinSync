# QA Results — SkinSync (round: 2025-10-08)

## Round summary
- Focus: manual testing of main user flows (registration/login, symptoms → results, PDF), basic validations, quick Network/Console check, and a mobile viewport pass.
- Status: no network errors (200 OK requests), no Console errors (Incognito), mobile layout stable. A few UX/Validation improvements have been opened as issues.

## Evidence (screenshots)
- Network: [SS-2025-10-08-network-clean.png](./qa/evidence/SS-2025-10-08-network-clean.png)
- Landing: [SS-2025-10-08-meta-landing.png](./qa/evidence/SS-2025-10-08-meta-landing.png)
- Registration (valid): [SS-2025-10-08-TC001-registration-valid.png](./qa/evidence/SS-2025-10-08-TC001-registration-valid.png)
- Registration (existing/invalid): [SS-2025-10-08-TC002-registration-invalid.png](./qa/evidence/SS-2025-10-08-TC002-registration-invalid.png)
- Login (valid): [SS-2025-10-08-TC003-login-valid.png](./qa/evidence/SS-2025-10-08-TC003-login-valid.png)
- Symptoms (form): [SS-2025-10-08-TC005-symptoms-form.png](./qa/evidence/SS-2025-10-08-TC005-symptoms-form.png)
- Results: [SS-2025-10-08-TC007-results-view.png](./qa/evidence/SS-2025-10-08-TC007-results-view.png)
- PDF (generated via Profile after sign‑in): [SS-2025-10-08-TC008-pdf-generated.png](./qa/evidence/SS-2025-10-08-TC008-pdf-generated.png)
- Mobile (iPhone 12): [SS-2025-10-08-TC010-mobile-view.png](./qa/evidence/SS-2025-10-08-TC010-mobile-view.png)
- Console: [SS-2025-10-08-console-clean.png](./qa/evidence/SS-2025-10-08-console-clean.png)

## Observations (concise)
- Network/Console:
  - Network: all requests 200 OK, no errors.
  - Console: no red errors on refresh (Incognito).
- Functional:
  - PDF becomes available after the user signs in and visits the Profile page (current logic).
  - The Results page does not offer a PDF button even for signed‑in users — UX suggestion: show “Download PDF” here as well.
  - Submitting with no symptoms/body parts would benefit from a clear validation message.
- Content/UX:
  - Suggest adding a short medical disclaimer near the form/results (“Informational only — not a medical diagnosis.”) and a brief privacy note about the PDF.
- Mobile:
  - Layout stable on iPhone 12; no horizontal scroll observed.

## Open issues (2025‑10‑08)
- [#1 UX — Show “Download PDF” on Results page for signed‑in users](https://github.com/lucijatoldi/SkinSync/issues/1)
- [#2 Validation — Clear message when no symptoms/body parts are selected](https://github.com/lucijatoldi/SkinSync/issues/2)
- [#3 Content — Add medical disclaimer and short privacy note](https://github.com/lucijatoldi/SkinSync/issues/3)
