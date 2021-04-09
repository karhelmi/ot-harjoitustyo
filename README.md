# <h1> Ohjelmistotekniikka, harjoitustyö

##<h2> Yleistä
Status: Ohjelma on työn alla

Olen tehnyt tämän ohjelman Ohjelmistotekniikan kurssin harjoitustyönä noin 6 viikon aikana keväällä 2021.
Tämä on ensimmäinen tekemäni tämänkaltainen sovellus.

Sovellus on vaate- ja tarvikerekisteri...[lisätään myöhemmin]



##<H2> Dokumentaatio

* [Vaatimusmäärittely](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) (Linkki harjoitustyön alustavaan määrittelydokumenttiin)
* [Työaikakirjanpito](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

##<h2> Komentorivitoiminnot ohjelmalle:
Invoke-työkalu on otettu käyttöön. Voit varmistaa Invoken avulla käytössä olevat komennot komennolla "poetry run invoke --list".
Ne sisältävät ainakin:
* start
* test
* coverage
* coverage-report

#<h3> Suorittaminen ja käynnistäminen#
Ohjelma käynnistyy komennolla

##poetry run invoke start##

#<h3> Testaus

##poetry run invoke test##

#<h3> Testikattavuus#

##poetry run invoke coverage-report## >> Testikattavuusraportti on nimeltään "index.html"-tiedosto juurihakemiston kansiossa "htmlcov")


