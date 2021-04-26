# Ohjelmistotekniikka, harjoitustyö (periodi 4, kevät 2021)

## Status

Ohjelma on työn alla. Käyttäjä voi tällä hetkellä lisätä uuden käyttäjätunnuksen, kirjautua sisään, tarkastella tarvikelistaa, lisätä uusia tarvikkeita listaan sekä kirjautua ulos. Tämän jälkeen käyttäjä voi halutessaan kirjautua takaisin sisään jne.

## Huomioitavaa

Repositorion data-hakemisto ei ole ylimääräinen, koska tietokanta luodaan tähän kansioon. (Viikon 3 palautteessa se oli määritetty "ylimääräiseksi tavaraksi".) Projektin testikattavuusraportinkin pitäisi nyt onnistua mielestäni. Omalla koneellani kaikki toimii kyllä.

## Python-versio
Käyttäjällä tulee olla Python versio 3.6 tai suurempi, jotta ohjelma toimii.

## Yleistä
  
Olen tekemässä tätä ohjelmaa Ohjelmistotekniikan kurssin harjoitustyönä noin 6 viikon aikana keväällä 2021.
Tämä on ensimmäinen tekemäni tämänkaltainen sovellus.

Sovellus on lasten vaate- ja tarvikerekisteri, jonka avulla käyttäjä voi lisätä omalla "sivustollaan" vaatekappale- tai tarvikekohtaista tietoa. Tavoitteena on myös rakentaa erinäisiä toimintoja lisätyille tiedoille. Lisätietoja löydät esimerkiksi Vaatimusmäärittely-dokumentista (linkki alla).

## Dokumentaatio
  
* [Vaatimusmäärittely](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) (linkki harjoitustyön alustavaan määrittelydokumenttiin)
* [Työaikakirjanpito](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
* [Luokkakaavio ja sekvenssikaavioita ohjelman rakenteesta](https://github.com/karhelmi/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Release-linkki
[Tässä](https://github.com/karhelmi/ot-harjoitustyo/releases/tag/viikko5) on linkki ohjelman ensimmäiseen releaseen ("Viikon 5 ohjelmaversion release"). Lataa lähdekoodi koneellesi. Mene tämän jälkeen lataamasi lähdekoodin juurihakemistoon komentoriviltäsi, ja suorita seuraavassa kohdassa kerrotut asennusohjeet.

## Asennusohjeet Releasea varten
1. Asenna riippuvuudet komennolla: **poetry install**
2. Tämän jälkeen voit käynnistää ohjelman komennolla: **poetry run invoke start**

Huomaa, että tällä hetkellä ohjelma alustaa tietokannan aina käynnistyksen yhteydessä. Tämä tarkoittaa, että sulkiessasi ohjelman (ruudun kulman ruksilla) tietokanta häviää eli suorittaessasi komennon "poetry run invoke start", ohjelmaa aina alustaa tietokannan.
Lisää komentorivitoimintoja on esitetty alla seuraavassa kohdassa.

## Komentorivitoiminnot ohjelmalle
  
Invoke-työkalu on otettu käyttöön. Voit varmistaa Invoken avulla käytössä olevat komennot komennolla "poetry run invoke --list".
Ne sisältävät ainakin:
* start (suorittaa / aloittaa ohjelman)
* test (suorittaa koodin automaattisen testit)
* coverage (kerää testikattavuuden "pytest src" -komennon suorittamista testeistä)
* coverage-report (luo graafisen testikattavuusraportin tiedostoon index.html htmlcov-kansioon)
* lint (suorittaa koodin laadun staattisen analyysin)
* format (formatoi src-kansion koodin PEP8-tyyliohjeiden mukaisesti)

### 1. Suorittaminen ja käynnistäminen

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
