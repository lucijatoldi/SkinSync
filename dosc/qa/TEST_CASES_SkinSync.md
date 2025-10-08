# Test Cases — SkinSync (core)

| ID     | Title                                  | Preconditions          | Steps                                                                | Expected |
|--------|----------------------------------------|------------------------|----------------------------------------------------------------------|---------|
| TC-001 | Registration (valid)                   | App is available       | Open Registration → fill valid fields → Submit                       | Account created; success/redirect |
| TC-002 | Registration (existing username)       | Username already taken | Open Registration → use existing username → Submit                   | Clear message “Username already taken” |
| TC-003 | Login (valid credentials)              | Account exists         | Open Login → enter correct credentials → Submit                      | Successful login |
| TC-004 | Login (wrong password)                 | Account exists         | Open Login → enter wrong password → Submit                           | Error message; no login |
| TC-005 | Symptoms (minimal selection)           | Signed‑in user         | Open form → select minimal valid combo → Submit                      | Reasonable results or clear “no matches” |
| TC-006 | Symptoms (no selection)                | Signed‑in user         | Open form → select nothing → Submit                                  | Validation message shown (tracked in Issue #2) |
| TC-007 | Results (content)                      | Results exist          | After Submit → review list                                           | Disease names, suggested treatments and triggers (if defined) |
| TC-008 | PDF (signed‑in flow)                   | Signed‑in, has results | Submit form → go to Profile                                          | PDF file is present/available for download |
| TC-009 | PDF (signed‑out)                       | Signed‑out             | Try to access Profile or PDF                                         | Redirect to login or message; PDF not offered on Results |
| TC-010 | Mobile view (basic)                    | —                      | DevTools → iPhone 12 → key pages                                     | Readable UI, no layout break or horizontal scroll |

Notes:
- TC‑006 reflects a desired validation; current behavior may lack a message (see Issue #2).
- TC‑009 matches current logic (PDF via Profile for signed‑in users); Issue #1 proposes adding a PDF button to Results for signed‑in users.
