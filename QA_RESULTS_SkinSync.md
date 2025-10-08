# QA Results — SkinSync (runda: 2025-10-08)

## Sažetak runde
- Fokus: ručno testiranje glavnih tokova (registracija/prijava, simptomi → rezultati, PDF), osnovne validacije, brzi pogled na mrežu/konzolu i mobilni prikaz.
- Stanje: bez grešaka na mreži, bez errora u konzoli (local check), mobilni prikaz stabilan. Nekoliko UX/Validation prijedloga otvorit ću kao issue-e.

## Dokazi (screenshots)
- Network: [SS-2025-10-08-network-clean.png](./qa/evidence/SS-2025-10-08-network-clean.png)
- Landing: [SS-2025-10-08-meta-landing.png](./qa/evidence/SS-2025-10-08-meta-landing.png)
- Registracija (valjano): [SS-2025-10-08-TC001-registration-valid.png](./qa/evidence/SS-2025-10-08-TC001-registration-valid.png)
- Registracija (slabo/invalid): [SS-2025-10-08-TC002-registration-invalid.png](./qa/evidence/SS-2025-10-08-TC002-registration-invalid.png)
- Prijava (točno): [SS-2025-10-08-TC003-login-valid.png](./qa/evidence/SS-2025-10-08-TC003-login-valid.png)
- Simptomi (forma): [SS-2025-10-08-TC005-symptoms-form.png](./qa/evidence/SS-2025-10-08-TC005-symptoms-form.png)
- Rezultati: [SS-2025-10-08-TC007-results-view.png](./qa/evidence/SS-2025-10-08-TC007-results-view.png)
- PDF (generiran nakon profila): [SS-2025-10-08-TC008-pdf-generated.png](./qa/evidence/SS-2025-10-08-TC008-pdf-generated.png)
- Mobile (iPhone 12): [SS-2025-10-08-TC010-mobile-view.png](./qa/evidence/SS-2025-10-08-TC010-mobile-view.png)
- Console: (ako dodaš) [SS-2025-10-08-console-clean.png](./qa/evidence/SS-2025-10-08-console-clean.png)

## Opažanja (kratko)
- Network/Console:
  - Network: svi zahtjevi 200 OK, bez grešaka.
  - Console: nije uočen crveni error na refreshu (Incognito).
- Funkcionalno:
  - PDF je dostupan nakon što se korisnik prijavi i ode na Profil (očekivano prema trenutnoj logici).
  - Stranica s rezultatima ne nudi PDF (za prijavljene) — UX ideja: prikaz gumba “Preuzmi PDF” i ovdje.
  - Kada se formu pošalje bez odabira simptoma/dijelova, korisniku bi koristila jasna poruka (“Odaberite barem jedan simptom i dio tijela.”).
- Sadržaj/UX:
  - Preporuka dodati kratki “disclaimer” uz formu/rezultate (“Informativno — nije zamjena za liječničku dijagnozu.”).
- Mobilno:
  - Layout stabilan; bez horizontalnog skrola u iPhone 12 prikazu.

## Predloženi issue-i
- [UX] Rezultati: prikaz “Preuzmi PDF” gumba za prijavljene korisnike
- [Validation] Poruka kada nema odabranih simptoma/dijelova
- [Content] Dodati medicinski disclaimer i napomenu o privatnosti (PDF)
- [A11y] Provjeriti vidljiv fokus i klikabilne labele (poboljšanje)
