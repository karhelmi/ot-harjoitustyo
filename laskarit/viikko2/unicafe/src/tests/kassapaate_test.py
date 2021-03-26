import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassa_oikea_rahamaara(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_luotu_kassa_nolla_maukasta(self):
        self.assertEqual((self.kassapaate.maukkaat), 0)

    def test_luotu_kassa_nolla_edullista(self):
        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test_kateisosto_edullisesti_kassa_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_edullisesti__vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(vaihtoraha, 760)

    def test_kateisosto_maukas_kassa_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_maukas_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(vaihtoraha, 600)

    def test_kateisosto_edullisesti_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_maukas_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_maukas_maksu_ei_riita_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_edullinen_maksu_ei_riita_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_maukas_maksu_ei_riita_vaihtoraha_kokomaksu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_kateisosto_edullinen_maksu_ei_riita_vaihtoraha_kokomaksu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kateisosto_maukas_maksu_ei_riita_lounasmaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_maksu_ei_riita_lounasmaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

#Korttimaksujen testit tämän alapuolella:

    def test_korttiosto_edullisesti_veloitus_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_korttiosto_edullisesti_palauttaa_True(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_korttiosto_maukkaasti_veloitus_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_korttiosto_maukkaasti_palauttaa_True(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
#
    def test_korttiosto_edullisesti_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_maukas_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
#
    def test_korttiosto_maukas_kortilla_ei_tarpeeksirahaa_kortinsaldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)

    def test_korttiosto_edullinen_kortilla_ei_tarpeeksirahaa_kortinsaldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 200)
#
    def test_korttiosto_maukas_kortilla_ei_tarpeeksirahaa_lounasmaara_ei_muutu(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_kortilla_ei_tarpeeksirahaa_lounasmaara_ei_muutu(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
#
    def test_korttiosto_maukas_kortilla_ei_tarpeeksirahaa_palauttaa_False(self):
        self.maksukortti.ota_rahaa(800)
        palautus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(palautus, False)

    def test_korttiosto_edullinen_kortilla_ei_tarpeeksirahaa_palauttaa_False(self):
        self.maksukortti.ota_rahaa(800)
        palautus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(palautus, False)
#
    def test_korttiosto_maukas_kassasaldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_edullinen_kassasaldo_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
#

    def test_lataa_rahaa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,500)
        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_lataa_rahaa_kortille_kassamaara_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

#Lisään oman, jotta testikattavuus on 100%:
    def test_lataa_neg_summan_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-500)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataa_neg_summan_kassan_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

