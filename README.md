# Miinaharava

Miinaharava on muun muassa vanhoista Windows-versioista tuttu peli *Minesweeper*. Pelin tavoitteena on paljastaa kaikki ruudut, joiden alla ei ole miinaa. Jos paljastaa miinan, häviää pelin. Pelissä pystyy myös liputtamaan miinaksi epäiltyjä ruutuja.

## Pythonin ja poetryn versiot
Ohjelmaan tarvitaan vähintään pythonin versio 3.8. Ohjelma on julkaistu poetryn version 1.4.2 kanssa. Vanhemmilla versioilla saattaa ilmetä ongelmia.


## Loppupalautuksen release
[Release löytyy tästä linkistä](https://github.com/thefakejj/Minesweeper/releases/tag/v1.0.0)


## Dokumentaatio
- [Käyttöohje](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/kayttoohje.md)
- [Tuntikirjanpito](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/vaatimusmaarittely.md)
- [Changelog](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/arkkitehtuurikuvaus.md)
- [Testausdokumentaatio](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/testaus.md)

## Asennusohjeet

### Ohjelman käyttämiseen tarvitaan Poetry. Kaikki komennot tulee ajaa ohjelman juurihakemistossa (minesweeper).

1: Mene virtuaaliympäristöön

```bash
poetry shell
```

2: Asenna riippuvuudet

```bash
poetry install
```

3: Luo tietokanta. HUOM: Tämä komento tyhjentää sen tietokannan, minkä tiedostonimi on .envissä! 

```bash
poetry run invoke build
```

4: Nyt kun ohjelma on asennettu, voit käynnistää sen komennolla:

```bash
poetry run invoke start
```
Tästä eteenpäin ohjelman voi käynnistää ajamalla vain tämän komennon.

<br>

## Muut komennot

### Luo koodin testikattavuusraportti komennolla:
```bash
poetry run invoke coverage-report
```
Testikattavuusraportti näkyy sen jälkeen hakemistossa htmlcov. Voit avata tiedoston index.html katsoaksesi raporttia.

<br>

### Tarkista koodin laatu komennolla:
```bash
poetry run invoke lint
```
Tarkistukset on määritelty tiedostossa .pylintrc
