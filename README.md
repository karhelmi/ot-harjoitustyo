# Ohjelmistotekniikka, harjoitustyö (periodi 4, kevät 2021)

## Status

Ohjelma on työn alla. Create new user -toiminto toimii, kun laittaja kirjoittaa käyttäjänimen ja salasanan niille avautuvaan ikkunaan. Ikkuna tulee sulkea oikeasta yläkulmasta, jolloin ohjelma suorittaa lisäyksen.

## Yleistä
  
Olen tehnyt tämän ohjelman Ohjelmistotekniikan kurssin harjoitustyönä noin 6 viikon aikana keväällä 2021.
Tämä on ensimmäinen tekemäni tämänkaltainen sovellus.

Sovellus on lasten vaate- ja tarvikerekisteri, jonka avulla käyttäjä voi lisätä omalla "sivustollaan" vaatekappale- tai tarvikekohtaista tietoa. Tavoitteena on myös rakentaa erinäisiä toimintoja lisätyille tiedoille.

## Dokumentaatio
  
* [Vaatimusmäärittely](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) (linkki harjoitustyön alustavaan määrittelydokumenttiin)
* [Työaikakirjanpito](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

## Komentorivitoiminnot ohjelmalle:
  
Invoke-työkalu on otettu käyttöön. Voit varmistaa Invoken avulla käytössä olevat komennot komennolla "poetry run invoke --list".
Ne sisältävät ainakin:
* start
* test
* coverage
* coverage-report

### Suorittaminen ja käynnistäminen

Ohjelma käynnistyy komennolla

poetry run invoke start

### Testaus

poetry run invoke test

### Testikattavuus
  
poetry run invoke coverage-report >> Testikattavuusraportti on nimeltään "index.html"-tiedosto juurihakemiston kansiossa "htmlcov")
