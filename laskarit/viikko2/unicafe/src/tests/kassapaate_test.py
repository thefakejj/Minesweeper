import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.ed_riittaa = Maksukortti(250)
        self.ed_ei_riita = Maksukortti(230)
        self.mau_riittaa = Maksukortti(410)
        self.mau_ei_riita = Maksukortti(390)

    def test_rahamaara_ja_myydyt_lounaat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(390), 390)

    def test_korttiosto_toimii(self):
        myydyt_edulliset = self.kassapaate.edulliset
        myydyt_maukkaat = self.kassapaate.maukkaat
        kassan_rahat = self.kassapaate.kassassa_rahaa

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.ed_riittaa), True)
        self.assertEqual(str(self.ed_riittaa), "Kortilla on rahaa 0.10 euroa")
        self.assertEqual(self.kassapaate.edulliset, myydyt_edulliset+1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, kassan_rahat)
        myydyt_edulliset += 1
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.ed_ei_riita), False)
        self.assertEqual(str(self.ed_ei_riita), "Kortilla on rahaa 2.30 euroa")
        self.assertEqual(self.kassapaate.edulliset, myydyt_edulliset)
        self.assertEqual(self.kassapaate.kassassa_rahaa, kassan_rahat)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.mau_riittaa), True)
        self.assertEqual(str(self.mau_riittaa), "Kortilla on rahaa 0.10 euroa")
        self.assertEqual(self.kassapaate.maukkaat, myydyt_maukkaat+1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, kassan_rahat)
        myydyt_maukkaat += 1
        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.mau_ei_riita), False)
        self.assertEqual(str(self.mau_ei_riita), "Kortilla on rahaa 3.90 euroa")
        self.assertEqual(self.kassapaate.maukkaat, myydyt_maukkaat)
        self.assertEqual(self.kassapaate.kassassa_rahaa, kassan_rahat)

    def test_rahan_lataus_kortin_saldo_muuttuu_kassan_rahamaara_kasvaa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.ed_riittaa, -100)
        self.assertEqual(str(self.ed_riittaa), "Kortilla on rahaa 2.50 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.kassapaate.lataa_rahaa_kortille(self.ed_riittaa, 0)
        self.assertEqual(str(self.ed_riittaa), "Kortilla on rahaa 2.50 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
        self.kassapaate.lataa_rahaa_kortille(self.ed_riittaa, 50)
        self.assertEqual(str(self.ed_riittaa), "Kortilla on rahaa 3.00 euroa")