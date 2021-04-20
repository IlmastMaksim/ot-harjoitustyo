import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        saldo_euroissa = round(10 / 100, 2)
        self.assertEqual(str(self.maksukortti), f"saldo: {saldo_euroissa}")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2)
        saldo_euroissa = round(12 / 100, 2)
        self.assertEqual(str(self.maksukortti), f"saldo: {saldo_euroissa}")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(6)
        saldo_euroissa = round(4 / 100, 2)
        self.assertEqual(str(self.maksukortti), f"saldo: {saldo_euroissa}")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(6)
        self.maksukortti.ota_rahaa(6)
        saldo_euroissa = round(4 / 100, 2)
        self.assertEqual(str(self.maksukortti), f"saldo: {saldo_euroissa}")

    def test_true_jos_rahat_riittivat(self):
        palautus = self.maksukortti.ota_rahaa(6)
        self.assertEqual(palautus, True)

    def test_false_jos_rahat_ei_riita(self):
        kortti = Maksukortti(2)
        palautus = kortti.ota_rahaa(6)
        self.assertEqual(palautus, False)
