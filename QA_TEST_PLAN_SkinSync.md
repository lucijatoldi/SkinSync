# QA Test Plan — SkinSync

## Sažetak
Cilj: provjeriti osnovnu ispravnost ključnih tokova (registracija/prijava, unos simptoma, rezultati, PDF). Pristup: ručno testiranje (happy path + osnovni negativni slučajevi) i kratke UX napomene.

## Opseg
U opsegu:
- Registracija i prijava
- Forma sa simptomima i prikaz rezultata
- Generiranje PDF-a (prijavljeni korisnik)
- Osnovne validacije i poruke o greškama

Izvan opsega (u ovoj iteraciji):
- Automatizacija, performance, sigurnosni i mobilni nativni testovi

## Okruženja
- Live: https://skinsync-production.up.railway.app

## Pristup testiranju
- Exploratory prolaz kako bi se uočile brze nepravilnosti
- Kratki testni slučajevi s jasnim, ponovljivim koracima
- Dokazi (screenshotovi) u mapi `qa/evidence`

## Test podaci (primjeri)
- Korisnik: test.user@example.com / Lozinka: Test12345!
- Simptomi: kombinacije koje očekivano daju 0, 1 i više rezultata

## Kriteriji završetka
- Izvršeni planirani test slučajevi
- Otvoreni issue-i za uočene probleme (koraci, očekivano/stvarno, dokaz)
