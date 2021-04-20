# Ohjelmistotekniikka, harjoitustyö (periodi 4, kevät 2021)

## Status

Ohjelma on työn alla. Create new user -toiminto toimii, kun laittaja kirjoittaa käyttäjänimen ja salasanan niille avautuvaan ikkunaan. Ikkuna tulee sulkea oikeasta yläkulmasta, jolloin ohjelma suorittaa lisäyksen.

## Yleistä
  
Olen tehnyt tämän ohjelman Ohjelmistotekniikan kurssin harjoitustyönä noin 6 viikon aikana keväällä 2021.
Tämä on ensimmäinen tekemäni tämänkaltainen sovellus.

Sovellus on lasten vaate- ja tarvikerekisteri, jonka avulla käyttäjä voi lisätä omalla "sivustollaan" vaatekappale- tai tarvikekohtaista tietoa. Tavoitteena on myös rakentaa erinäisiä toimintoja lisätyille tiedoille. Lisätietoja löydät esimerkiksi Vaatimusmäärittely-dokumentista (linkki alla).

## Dokumentaatio
  
* [Vaatimusmäärittely](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) (linkki harjoitustyön alustavaan määrittelydokumenttiin)
* [Työaikakirjanpito](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
* [Luokkakaavio ohjelman rakenteesta]((https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Komentorivitoiminnot ohjelmalle
  
Invoke-työkalu on otettu käyttöön. Voit varmistaa Invoken avulla käytössä olevat komennot komennolla "poetry run invoke --list".
Ne sisältävät ainakin:
* start (suorittaa / aloittaa ohjelman)
* test (suorittaa koodin automaattisen testit)
* coverage (kerää testikattavuuden "pytest src" -komennon suorittamista testeistä)
* coverage-report (luo graafisen testikattavuusraportin tiedostoon index.html htmlcov-kansioon)
* lint (suorittaa koodin laadun staattisen analyysin)
* format (formatoi src-kansion koodin PEP8 -tyyliohjeiden mukaisesti)

### 1. Suorittaminen ja käynnistäminen

Ohjelma käynnistyy komennolla: **poetry run invoke start**

### 2. Testaus

Ohjelman toimivuutta voi testata komennolla: **poetry run invoke test**

### 3. Testikattavuus

Testikattavuusraportin saa komennolla: **poetry run invoke coverage-report**

Testikattavuusraportti on nimeltään "index.html"-tiedosto juurihakemiston kansiossa "htmlcov". 
