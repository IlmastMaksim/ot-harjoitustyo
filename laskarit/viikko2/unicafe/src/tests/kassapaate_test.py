
import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luodun_kassapaatteen_rahamaara_ja_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_toimii_maukkaiden_lounaiden_osalta(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(palautus, 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        palautus2 = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(palautus2, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)


    def test_kateisosto_toimii_edullisten_lounaiden_osalta(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(palautus, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        palautus2 = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(palautus2, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_toimii__edullisten_lounaiden_osalta(self):
        maksukortti = Maksukortti(50000)
        korttiosto = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(korttiosto, True)
        self.assertEqual(maksukortti.saldo, 50000-240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        maksukortti2 = Maksukortti(100)
        korttiosto2 = self.kassapaate.syo_edullisesti_kortilla(maksukortti2)
        self.assertEqual(korttiosto2, False)
        self.assertEqual(maksukortti2.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii__maukkaiden_lounaiden_osalta(self):
        maksukortti = Maksukortti(50000)
        korttiosto = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(korttiosto, True)
        self.assertEqual(maksukortti.saldo, 50000-400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        maksukortti2 = Maksukortti(100)
        korttiosto2 = self.kassapaate.syo_maukkaasti_kortilla(maksukortti2)
        self.assertEqual(korttiosto2, False)
        self.assertEqual(maksukortti2.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_rahaa_ladattaessa(self):
        maksukortti = Maksukortti(50000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 10000)
        self.assertEqual(maksukortti.saldo, 60000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 10000)
        palautus = self.kassapaate.lataa_rahaa_kortille(maksukortti, -10000)
        self.assertEqual(palautus, None)
        

            
