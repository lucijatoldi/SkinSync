import rdflib

g = rdflib.Graph()

NS = rdflib.Namespace("http://example.org/ontology/")
g.bind("koza", NS)


# ===============================================
# === DEFINICIJA SVIH ENTITETA (IZVOR ISTINE) ===
# ===============================================

oboljenja = [
    "Dermatitis", "Psorijaza", "Akne", "Ekcem", "GljivicnaInfekcija", 
    "SeboreicniDermatitis", "KontaktniDermatitis", "HerpesZoster", 
    "Vitiligo", "Rosacea", "AlopeciaAreata", "Urtikarija", "Lupus", 
    "Folikulitis", "Impetigo", "AtopijskiDermatitis", "Tinea"
]

simptomi = [
    "Crvenilo", "Svrbez", "Osip", "PerutanjeKoze", "Plikovi", "SuhaKoza", 
    "PucanjeKoze", "Oticanje", "BolNaDodir", "PromjenaBojeKoze", 
    "LjuskanjeKoze", "GnojniPrist", "Mjehurici", "Peckanje", "Upala",
    "GubitakKose" 
]

dijelovi_tijela = [
    "Lice", "Ruke", "Noge", "Vlasiste", "Torzo", "Stopala", "Leda", 
    "Trbuh", "Prsa", "Ramena", "Vrat", "Pazusje", "Laktovi", "Dlanovi", 
    "Tabani", "Usne", "Koljena", "DonjiDioLeda", "Usi", "Rebra", 
    "Preponi", "Nokti", "Obrve", "Trepavice"
]

tretmani = [
    "TopikalniKortikosteroidi", "AntifungalnaKrema", "AntibiotskaMast", 
    "Antihistaminici", "OralniKortikosteroidi", "Imunomodulatori", 
    "SalicilnaKiselina", "Retinoidi", "Moisturizeri", "AntiviralniLijekovi", 
    "Fototerapija", "ZincOxide", "BenzoilPeroksid", "HidratantneKreme", 
    "KremaSaUreom", "OralniAntifungalniLijekovi", "SamponiSKetokonazolom",
    "Analgetici", "TopikalniMetronidazol", "OralniAntibiotici", "Imunoterapija",
    "Imunosupresivi", "Antimalarici", "TopikalniAntiseptici"
]

okidaci = [
    "Alergeni", "Stres", "HormonalnePromjene", "SuhaKoza", "Znojenje", 
    "Kemikalije", "Vrucina", "Hladnoca", "Vlaga", "Infekcije", 
    "NeprikladniKozmetickiProizvodi", "Sunce", "OdjecaOdSintetike", 
    "Prasina", "Grinje", "Alkohol", "NedostatakSna", "KlimatskePromjene"
]

# ======================================
# === DODAVANJE RELACIJA U ONTOLOGIJU ===
# ======================================

relacije = [
    # --- Oboljenja, simptomi i tretmani ---
    
    # Psorijaza
    (NS.Psorijaza, NS.ima_simptom, NS.Crvenilo),
    (NS.Psorijaza, NS.ima_simptom, NS.PerutanjeKoze),
    (NS.Psorijaza, NS.ima_simptom, NS.SuhaKoza),
    (NS.Psorijaza, NS.ima_simptom, NS.LjuskanjeKoze),
    (NS.Psorijaza, NS.preporučuje_tretman, NS.TopikalniKortikosteroidi),
    (NS.Psorijaza, NS.preporučuje_tretman, NS.Fototerapija),
    (NS.Psorijaza, NS.preporučuje_tretman, NS.Imunomodulatori),

    # Akne
    (NS.Akne, NS.ima_simptom, NS.GnojniPrist),
    (NS.Akne, NS.ima_simptom, NS.Crvenilo),
    (NS.Akne, NS.ima_simptom, NS.Upala),
    (NS.Akne, NS.preporučuje_tretman, NS.BenzoilPeroksid),
    (NS.Akne, NS.preporučuje_tretman, NS.AntibiotskaMast),
    (NS.Akne, NS.preporučuje_tretman, NS.Retinoidi),

    # Ekcem
    (NS.Ekcem, NS.ima_simptom, NS.Crvenilo),
    (NS.Ekcem, NS.ima_simptom, NS.Svrbez),
    (NS.Ekcem, NS.ima_simptom, NS.SuhaKoza),
    (NS.Ekcem, NS.ima_simptom, NS.Oticanje),
    (NS.Ekcem, NS.preporučuje_tretman, NS.TopikalniKortikosteroidi),
    (NS.Ekcem, NS.preporučuje_tretman, NS.Antihistaminici),
    (NS.Ekcem, NS.preporučuje_tretman, NS.Moisturizeri),

    # Gljivična Infekcija / Tinea
    (NS.GljivicnaInfekcija, NS.ima_simptom, NS.Crvenilo),
    (NS.GljivicnaInfekcija, NS.ima_simptom, NS.PerutanjeKoze),
    (NS.GljivicnaInfekcija, NS.ima_simptom, NS.Svrbez),
    (NS.GljivicnaInfekcija, NS.preporučuje_tretman, NS.AntifungalnaKrema),
    (NS.GljivicnaInfekcija, NS.preporučuje_tretman, NS.OralniAntifungalniLijekovi),
    (NS.Tinea, NS.ima_simptom, NS.Crvenilo), # Tinea je vrsta gljivične infekcije
    (NS.Tinea, NS.ima_simptom, NS.Svrbez),
    (NS.Tinea, NS.preporučuje_tretman, NS.AntifungalnaKrema),


    # Seboreični Dermatitis
    (NS.SeboreicniDermatitis, NS.ima_simptom, NS.Crvenilo),
    (NS.SeboreicniDermatitis, NS.ima_simptom, NS.PerutanjeKoze),
    (NS.SeboreicniDermatitis, NS.ima_simptom, NS.Svrbez),
    (NS.SeboreicniDermatitis, NS.preporučuje_tretman, NS.AntifungalnaKrema),
    (NS.SeboreicniDermatitis, NS.preporučuje_tretman, NS.SamponiSKetokonazolom),

    # Kontaktni Dermatitis
    (NS.KontaktniDermatitis, NS.ima_simptom, NS.Crvenilo),
    (NS.KontaktniDermatitis, NS.ima_simptom, NS.Svrbez),
    (NS.KontaktniDermatitis, NS.ima_simptom, NS.Oticanje),
    (NS.KontaktniDermatitis, NS.ima_simptom, NS.Plikovi),
    (NS.KontaktniDermatitis, NS.preporučuje_tretman, NS.TopikalniKortikosteroidi),
    (NS.KontaktniDermatitis, NS.preporučuje_tretman, NS.Moisturizeri),

    # Herpes Zoster
    (NS.HerpesZoster, NS.ima_simptom, NS.Crvenilo),
    (NS.HerpesZoster, NS.ima_simptom, NS.Plikovi),
    (NS.HerpesZoster, NS.ima_simptom, NS.BolNaDodir),
    (NS.HerpesZoster, NS.ima_simptom, NS.Peckanje),
    (NS.HerpesZoster, NS.preporučuje_tretman, NS.AntiviralniLijekovi),
    (NS.HerpesZoster, NS.preporučuje_tretman, NS.Analgetici),

    # Vitiligo
    (NS.Vitiligo, NS.ima_simptom, NS.PromjenaBojeKoze),
    (NS.Vitiligo, NS.preporučuje_tretman, NS.TopikalniKortikosteroidi),
    (NS.Vitiligo, NS.preporučuje_tretman, NS.Fototerapija),

    # Rosacea
    (NS.Rosacea, NS.ima_simptom, NS.Crvenilo),
    (NS.Rosacea, NS.ima_simptom, NS.Peckanje),
    (NS.Rosacea, NS.ima_simptom, NS.Upala),
    (NS.Rosacea, NS.preporučuje_tretman, NS.TopikalniMetronidazol),
    (NS.Rosacea, NS.preporučuje_tretman, NS.OralniAntibiotici),

    # Alopecia Areata
    (NS.AlopeciaAreata, NS.ima_simptom, NS.GubitakKose),
    (NS.AlopeciaAreata, NS.preporučuje_tretman, NS.TopikalniKortikosteroidi),
    (NS.AlopeciaAreata, NS.preporučuje_tretman, NS.Imunoterapija),

    # Urtikarija (Koprivnjača)
    (NS.Urtikarija, NS.ima_simptom, NS.Crvenilo),
    (NS.Urtikarija, NS.ima_simptom, NS.Svrbez),
    (NS.Urtikarija, NS.ima_simptom, NS.Oticanje),
    (NS.Urtikarija, NS.preporučuje_tretman, NS.Antihistaminici),

    # Lupus
    (NS.Lupus, NS.ima_simptom, NS.Osip),
    (NS.Lupus, NS.ima_simptom, NS.PromjenaBojeKoze),
    (NS.Lupus, NS.preporučuje_tretman, NS.Imunosupresivi),
    (NS.Lupus, NS.preporučuje_tretman, NS.Antimalarici),

    # Folikulitis
    (NS.Folikulitis, NS.ima_simptom, NS.Crvenilo),
    (NS.Folikulitis, NS.ima_simptom, NS.GnojniPrist),
    (NS.Folikulitis, NS.ima_simptom, NS.Svrbez),
    (NS.Folikulitis, NS.preporučuje_tretman, NS.AntibiotskaMast),

    # Impetigo
    (NS.Impetigo, NS.ima_simptom, NS.Plikovi),
    (NS.Impetigo, NS.ima_simptom, NS.GnojniPrist),
    (NS.Impetigo, NS.preporučuje_tretman, NS.AntibiotskaMast),

    # --- Lokacije na tijelu ---
    (NS.Psorijaza, NS.pojavljuje_se_na, NS.Laktovi),
    (NS.Psorijaza, NS.pojavljuje_se_na, NS.Koljena),
    (NS.Psorijaza, NS.pojavljuje_se_na, NS.Vlasiste),
    (NS.Psorijaza, NS.pojavljuje_se_na, NS.Leda),

    (NS.Akne, NS.pojavljuje_se_na, NS.Lice),
    (NS.Akne, NS.pojavljuje_se_na, NS.Leda),
    (NS.Akne, NS.pojavljuje_se_na, NS.Prsa),
    (NS.Akne, NS.pojavljuje_se_na, NS.Ramena),

    (NS.Ekcem, NS.pojavljuje_se_na, NS.Ruke),
    (NS.Ekcem, NS.pojavljuje_se_na, NS.Noge),
    (NS.Ekcem, NS.pojavljuje_se_na, NS.Lice),
    (NS.Ekcem, NS.pojavljuje_se_na, NS.Vrat),

    (NS.Rosacea, NS.pojavljuje_se_na, NS.Lice),
    (NS.Folikulitis, NS.pojavljuje_se_na, NS.Vlasiste),
    (NS.Folikulitis, NS.pojavljuje_se_na, NS.Pazusje),
    (NS.Folikulitis, NS.pojavljuje_se_na, NS.Noge),
    
    (NS.Tinea, NS.pojavljuje_se_na, NS.Vlasiste),
    (NS.Tinea, NS.pojavljuje_se_na, NS.Stopala),
    (NS.Tinea, NS.pojavljuje_se_na, NS.Preponi),

    (NS.HerpesZoster, NS.pojavljuje_se_na, NS.Torzo),
    (NS.HerpesZoster, NS.pojavljuje_se_na, NS.Rebra),
    (NS.HerpesZoster, NS.pojavljuje_se_na, NS.Lice),

    # --- Okidači ---
    (NS.Alergeni, NS.pogoršava, NS.Ekcem),
    (NS.Alergeni, NS.pogoršava, NS.Urtikarija),
    (NS.Alergeni, NS.pogoršava, NS.KontaktniDermatitis),
    
    (NS.Stres, NS.pogoršava, NS.Psorijaza),
    (NS.Stres, NS.pogoršava, NS.Ekcem),
    (NS.Stres, NS.pogoršava, NS.Rosacea),
    (NS.Stres, NS.pogoršava, NS.Urtikarija),

    (NS.HormonalnePromjene, NS.pogoršava, NS.Akne),
    (NS.SuhaKoza, NS.pogoršava, NS.Ekcem),
    (NS.Znojenje, NS.pogoršava, NS.Akne),
    (NS.Kemikalije, NS.pogoršava, NS.KontaktniDermatitis),
    (NS.Vrucina, NS.pogoršava, NS.Rosacea),
    (NS.Sunce, NS.pogoršava, NS.Rosacea),
    (NS.Sunce, NS.pogoršava, NS.Lupus),
    (NS.Alkohol, NS.pogoršava, NS.Rosacea),
]

for relacija in relacije:
    g.add(relacija)