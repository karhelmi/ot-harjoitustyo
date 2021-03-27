# Alustava määrittelydokumentti: Vaatimusmäärittely

## Sovelluksen tarkoitus

>  Lasten kanssa elämä on yhtä välineurheilua. 
>  Sovelluksen tarkoitus on helpottaa ja tehostaa tätä välineurheilua.

Sovellus on lastenvaate- ja tarvikerekisteri. Sovelluksen avulla käyttäjä voi pitää kirjaa organisoidusti lasten vaatteista, kengistä ja välineistä (esim. sukset) ja niihin liittyvistä yksityiskohdista. Sovelluksen avulla käyttäjä voi etsiä haluamaansa lasten vaatteisiin ja tarvikkeisiin liittyvää tietoa helposti ja nopeasti.

## Sovelluksen käyttäjät

Sovelluksella on ensi vaiheessa yksi käyttäjärooli, joka on *normaali käyttäjä*. 

## Käyttöliittymäluonnos

Saako tähän kuvan.
![](./kuvat/Kayttoliittymaluonnos_vaatimusmaarittelyyn 27.3.21.png)

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

*Normaalikäyttäjä* voi kirjautua sisään omaan rekisteriinsä käyttäjätunnuksen ja salasanan avulla. Jos hänellä ei vielä ole käyttäjätunnuksia, hän voi mennä luomaan uuden käyttäjätunnuksen ja salasanan, jonka jälkeen hän voi kirjautua palveluun.

### Kirjautumisen jälkeen

Kirjautumisen jälkeen *normaalikäyttäjälle* avautuu alue, jolla hän näkee aiemmin sivustolle lisäämänsä vaatteet ja tarvikkeet sekä niihin liittyvät lisätiedot, jotka sisältävät ainakin seuraavat tiedot:
* suosikki (x, jos suosikki)
* tyyppi (vaate, kengät, tavara...)
* sisä/ulko(käyttöön)
* koko
* merkki
* väri
* sukupuoli (T, P, unisex)
* kunto (Kuin uusi, Hyvä, Tyydyttävä, Rikki)
* huomioitavaa

## Toimintaympäristön rajoitteet

Sovelluksen tulee toimia Linux-käyttöjärjestelmällä varustetussa tietokoneessa.
Kaikki sovelluksen tiedot talletetaan paikallisen koneen levylle.

## Jatkokehitysideoita ja muuta
1. *Normaalikäyttäjä* voi merkitä, jos hän on lainannut joitain vaatteita tai tavaroita joksikin aikaväliksi ja kenelle.
1. Voisi lisätä toisen käyttäjäroolin, joka olisi *vieraileva käyttäjä*. *Vieraileva käyttäjä* voisi luoda käyttäjätunnuksen ja päästä *normaalikäyttäjältä* saamaansa salasanaa vastaan katsomaan ja selaamaan kyseisen *normaalikäyttäjän* tietoja. *Vieraileva käyttäjä* voisi merkata omaan tauluunsa vaatteet ja tarvikkeet, joista on kiinnostunut.
1. Saatetaan laajentaa vielä esim. lasten huonekaluihin, rattaisiin jne.
