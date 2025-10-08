# QA Test Plan — SkinSync

## Summary
Goal: verify the basic correctness of key flows (registration/login, symptoms → results, PDF). Approach: manual testing (happy path + basic negative cases) plus brief UX notes.

## Scope
In scope:
- Registration and login
- Symptoms form and results display
- PDF generation (signed‑in user)
- Basic validations and error messages

Out of scope (this round):
- Test automation, performance, security and native mobile testing

## Environments
- Live: https://skinsync-production.up.railway.app

## Test approach
- Exploratory pass to catch obvious issues
- Short test cases with clear, repeatable steps
- Evidence (screenshots) stored under `qa/evidence`

## Test data (examples)
- User: test.user@example.com / Password: Test12345!
- Symptoms/body parts: combinations expected to yield 0, 1 or multiple results

## Exit criteria
- Planned test cases executed
- Issues opened for observed problems (steps, expected/actual, evidence)
