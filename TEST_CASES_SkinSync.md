# Test Cases — SkinSync (osnovni)

| ID     | Naziv                                 | Preduvjeti             | Koraci                                                                 | Očekivano |
|--------|---------------------------------------|------------------------|-------------------------------------------------------------------------|-----------|
| TC-001 | Registracija (valjano)                | Aplikacija dostupna    | Otvori Registraciju → ispuni valjano → Submit                          | Račun kreiran, preusmjeravanje/poruka |
| TC-002 | Registracija (slaba/prazna lozinka)   | —                      | Otvori Registraciju → unesi slabo/prazno → Submit                      | Jasna poruka o grešci, bez rušenja |
| TC-003 | Prijava (točni podaci)                | Račun postoji          | Otvori Prijavu → unesi točno → Submit                                  | Uspješna prijava |
| TC-004 | Prijava (pogrešna lozinka)            | Račun postoji          | Otvori Prijavu → unesi pogrešno → Submit                               | Poruka o neuspjeloj prijavi |
| TC-005 | Simptomi (minimalni odabir)           | Prijavljen korisnik    | Otvori formu → odaberi minimalno → Submit                              | Razumni rezultat ili jasna poruka |
| TC-006 | Simptomi (bez odabira)                | Prijavljen korisnik    | Otvori formu → ne odaberi ništa → Submit                               | Validacijska poruka |
| TC-007 | Rezultati (sadržaj)                   | Postoje rezultati      | Nakon Submit → pregled liste                                           | Nazivi, tretmani i okidači (ako predviđeno) |
| TC-008 | PDF (prijavljen)                      | Prijavljen, ima rezultate | Klik na “Generate PDF”                                               | PDF se generira/preuzima |
| TC-009 | PDF (odjavljen)                       | Odjavljen              | Pokušaj otvoriti/generirati PDF                                        | Traži prijavu ili prikladna poruka |
| TC-010 | Mobile prikaz (osnovno)               | —                      | DevTools → iPhone 12 → ključne stranice                                | UI čitljiv, bez lomljenja lay outa |
