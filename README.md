# Ohjelmistotekniikka, harjoitustyö (periodi 4, kevät 2021)

## Status

Ohjelman lopullisesta versiosta on muodostettu Release eikä ohjelmaa tulla kurssin puitteissa enää jatkokehittämään.

## Yleistä
  
Olen tehnyt ohjelman Helsingin yliopiston Ohjelmistotekniikan kurssin harjoitustyönä noin 6 viikon aikana keväällä 2021.Tämä on ensimmäinen tekemäni tämänkaltainen sovellus.

Sovellus on lastentarvikerekisteri, jonka avulla käyttäjä voi pitää kirjaa lastentarvikekohtaisesta tiedosta omalla sivustollaan. Toki ohjelmaa voi käyttää myös aikuisten tarvikkeille, mutta se on suunniteltu erityisesti lapsiperheiden avuksi. Katso lisätietoja ohjelman toiminnoista Vaatimusmäärittely-dokumentista (linkki alla).

## Python-versio

Käyttäjällä tulee olla Python versio 3.6 tai suurempi, jotta ohjelma toimii.

## Dokumentaatio
  
* [Vaatimusmäärittely](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
* [Arkkitehtuuridokumentti](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
* [Käyttöohjeet](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
* [Testausdokumentti](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

## Release-linkki
Ohjelman Release on saatavilla [täältä](UPDATE!).
Lataa lähdekoodi koneellesi ja katso tämän jälkeen suoritettavat asennusohjeet seuraavan otsikon alta.

Linkit aiempiin Releaseihin:

[Viikon 6 Release](https://github.com/karhelmi/ot-harjoitustyo/releases/tag/viikko6)
[Viikon 5 Release](https://github.com/karhelmi/ot-harjoitustyo/releases/tag/viikko5)

## Asennusohjeet Releasea varten

Mene lataamasi lähdekoodin juurihakemistoon "ot-harjoitustyo" komentoriviltäsi ja suorita siellä seuraavat komennot:

1. Asenna riippuvuudet komennolla: **poetry install**
2. Alusta tietokanta komennolla: **poetry run invoke initialize** (tämä tarvitsee tehdä vain kerran, vaikka käyttäisi komentoa 3. uudelleen)
3. Tämän jälkeen voit käynnistää ohjelman komennolla: **poetry run invoke start**

Lisää komentorivitoimintoja on esitetty alla seuraavassa kohdassa. Ohjelman käyttöohjeisiin on linkki yllä kohdassa "Dokumentaatio".

## Komentorivitoiminnot ohjelmalle
  
Invoke-työkalu on otettu käyttöön. Voit varmistaa Invoken avulla käytössä olevat komennot komennolla "poetry run invoke --list".
Ne sisältävät ainakin:
* initialize (alustaa ja luo tietokannan)
*  start (suorittaa / aloittaa ohjelman)
* test (suorittaa koodin automaattisen testit)
* coverage (kerää testikattavuuden "pytest src" -komennon suorittamista testeistä)
* coverage-report (luo graafisen testikattavuusraportin tiedostoon index.html htmlcov-kansioon)
* lint (suorittaa koodin laadun staattisen analyysin)
* format (formatoi src-kansion koodin PEP8-tyyliohjeiden mukaisesti)

### 1. Tietokannan alustaminen

Alusta ja luo ennen ohjelman käynnistämistä tietokanta komennolla: **poetry run invoke initialize**

### 2. Suorittaminen ja käynnistäminen

Ohjelma käynnistyy komennolla: **poetry run invoke start**

### 3. Testaus

Ohjelman toimivuutta voi testata komennolla: **poetry run invoke test**

### 4. Testikattavuus

Testikattavuusraportin saa komennolla: **poetry run invoke coverage-report**

Testikattavuusraportti on nimeltään "index.html"-tiedosto juurihakemiston kansiossa "htmlcov". 

### 5. Pylint
Koodin laadun staattisen analyysin voi suorittaa komennolla: **poetry run invoke lint**

Analyysissa käytettävät laadun tarkistukset on määritetty tiedostossa .pylintrc

### 6. PEP8-tyyliohjeiden soveltaminen koodin luettavuuden parantamiseksi
Koodin muotoilun PEP8-tyyliohjeiden mukaiseksi voi suorittaa komennolla: **poetry run invoke format**
