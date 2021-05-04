# Ohjelmistotekniikka, harjoitustyö (periodi 4, kevät 2021)

## Status

Ohjelma on työn alla. Käyttäjä voi tällä hetkellä lisätä uuden käyttäjätunnuksen, kirjautua sisään, tarkastella omaa tarvikelistaa, tarkastella omalta tarvikelistalta vain tietyntyyppisiä tarvikkeita, lisätä uusia tarvikkeita listaan sekä kirjautua ulos. Tämän jälkeen käyttäjä voi halutessaan kirjautua takaisin sisään jne. Käyttäjiä voi olla useita, ja jokaisella on omat listansa.

## Python-versio
Käyttäjällä tulee olla Python versio 3.6 tai suurempi, jotta ohjelma toimii.

## Yleistä
  
Olen tekemässä tätä ohjelmaa Ohjelmistotekniikan kurssin harjoitustyönä noin 6 viikon aikana keväällä 2021.
Tämä on ensimmäinen tekemäni tämänkaltainen sovellus.

Sovellus on lasten vaate- ja tarvikerekisteri, jonka avulla käyttäjä voi lisätä omalla "sivustollaan" vaatekappale- tai tarvikekohtaista tietoa. Tavoitteena on myös rakentaa erinäisiä toimintoja lisätyille tiedoille. Lisätietoja löydät esimerkiksi Vaatimusmäärittely-dokumentista (linkki alla).

## Dokumentaatio
  
* [Vaatimusmäärittely](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) (linkki harjoitustyön alustavaan määrittelydokumenttiin)
* [Työaikakirjanpito](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
* [Arkkitehtuuri-dokumentti](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
* [Käyttöohjeet](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohjeet.md)

## Release-linkki
Ohjelman viimeisin eli viikon 6 Release on saatavilla [täältä](https://github.com/karhelmi/ot-harjoitustyo/releases/tag/viikko6).
Lataa lähdekoodi koneellesi ja katso tämän jälkeen suoritettavat asennusohjeet seuraavan otsikon alta.

Linkit aiempiin Releaseihin:

[Viikon 5 Release](https://github.com/karhelmi/ot-harjoitustyo/releases/tag/viikko5)

## Asennusohjeet Releasea varten

Mene lataamasi lähdekoodin juurihakemistoon "ot-harjoitustyö" komentoriviltäsi ja suorita siellä seuraavat komennot:

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

### 2. Testaus

Ohjelman toimivuutta voi testata komennolla: **poetry run invoke test**

### 3. Testikattavuus

Testikattavuusraportin saa komennolla: **poetry run invoke coverage-report**

Testikattavuusraportti on nimeltään "index.html"-tiedosto juurihakemiston kansiossa "htmlcov". 

### 4. Pylint
Koodin laadun staattisen analyysin voi suorittaa komennolla: **poetry run invoke lint**

Analyysissa käytettävät laadun tarkistukset on määritetty tiedostossa .pylintrc

### 5. PEP8-tyyliohjeiden soveltaminen koodin luettavuuden parantamiseksi
Koodin muotoilun PEP8-tyyliohjeiden mukaiseksi voi suorittaa komennolla: **poetry run invoke format**
