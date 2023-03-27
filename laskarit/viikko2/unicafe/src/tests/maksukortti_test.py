import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

#rahan ottaminen toimii
    def test_rahan_ottaminen_toimii_raha_riittaa(self):
        self.maksukortti.ota_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")

    def test_rahan_ottaminen_toimii_ei_riita(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_ottaminen_toimii_metodin_palautus(self):

        raha_riittaa = Maksukortti(1000)

        self.assertEqual(raha_riittaa.ota_rahaa(1000), True)

        raha_ei_riita = Maksukortti(1000)

        self.assertEqual(raha_ei_riita.ota_rahaa(2000), False)






"""
Rahan ottaminen toimii:
    Metodi palauttaa True, jos rahat riittivät ja muuten False
Suorita testit terminaalissa virtuaaliympäristössä pytest src-komennolla.
"""