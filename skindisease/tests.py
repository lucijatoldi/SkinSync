from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rdflib import Graph, Namespace, URIRef
from .models import Profile
from .utils import pronadji_dijagnoze


def create_test_graph():
    g = Graph()
    NS = Namespace("http://example.org/ontology/")
    g.add((NS.Ekcem, NS.ima_simptom, NS.Crvenilo))
    g.add((NS.Ekcem, NS.pojavljuje_se_na, NS.Ruke))
    g.add((NS.Ekcem, NS.preporučuje_tretman, NS.Moisturizeri))
    g.add((NS.Alergeni, NS.pogoršava, NS.Ekcem))
    g.add((NS.Psorijaza, NS.ima_simptom, NS.Crvenilo))
    g.add((NS.Psorijaza, NS.pojavljuje_se_na, NS.Laktovi))
    return g


class SkinSyncUnitTests(TestCase):
    """
    Unit testovi koji testiraju izolirane dijelove logike.
    """
    
    def test_pronadji_dijagnoze_logika(self):
        """Testira pronalazi li funkcija točnu dijagnozu na lažnom grafu."""
        test_graph = create_test_graph()
        rezultati = pronadji_dijagnoze(test_graph, ["Crvenilo"], ["Ruke"])
        
        self.assertEqual(len(rezultati), 1)
        self.assertEqual(rezultati[0]['dijagnoza'], 'Ekcem')
        self.assertIn('Moisturizeri', rezultati[0]['tretmani'])

    def test_automatsko_kreiranje_profila_nakon_registracije(self):
        """
        Provjerava rade li signali ispravno.
        Testira kreira li se automatski 'Profile' objekt nakon kreiranja 'User' objekta.
        """
        
        user = User.objects.create_user(username='testuser', password='password123')
        
        # `hasattr` provjerava ima li objekt `user` atribut `profile`
        self.assertTrue(hasattr(user, 'profile'))
        self.assertIsInstance(user.profile, Profile)


class SkinSyncIntegrationTests(TestCase):
    """
    Integration testovi koji testiraju cijeli request-response ciklus.
    """
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testkorisnik', password='password123')

    def test_home_page_status_code(self):
        """Testira učitava li se početna stranica ispravno (status 200 OK)."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_dijagnoza_view_nakon_post_zahtjeva(self):
        """Testira prikazuje li se stranica s rezultatima nakon slanja forme."""
        podaci_forme = {'simptomi': ['Crvenilo'], 'dio_tijela': ['Ruke']}
        response = self.client.post(reverse('dijagnoza'), podaci_forme)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rezultat.html')
        
        self.assertContains(response, "Ekcem") 
    
    def test_profile_view_zahtijeva_prijavu(self):
        """Testira preusmjerava li stranica profila neprijavljenog korisnika na login."""
        response = self.client.get(reverse('profile'))
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/profile/')

    def test_profile_view_za_prijavljenog_korisnika(self):
        """Testira može li prijavljeni korisnik pristupiti svom profilu."""
        
        self.client.login(username='testkorisnik', password='password123')
        
        response = self.client.get(reverse('profile'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertContains(response, "Profil korisnika: testkorisnik")