# Miinaharava

Miinaharava on muun muassa vanhoista Windows-versioista tuttu peli *Minesweeper*. Pelin tavoitteena on paljastaa kaikki ruudut, joiden alla ei ole miinaa. Jos paljastaa miinan, häviää pelin. Pelissä pystyy myös liputtamaan miinaksi epäiltyjä ruutuja.


## Viikko 6 release!
[Release löytyy tästä linkistä](https://github.com/thefakejj/ot-harjoitustyo/releases/tag/viikko6)


## Dokumentaatio
- [Käyttöohje](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/kayttoohje.md)
- [Tuntikirjanpito](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/vaatimusmaarittely.md)
- [Changelog](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/thefakejj/ot-harjoitustyo/blob/main/documentation/arkkitehtuurikuvaus.md)

## Asennusohjeet

### Ohjelman käyttämiseen tarvitaan Poetry. Kaikki komennot tulee ajaa ohjelman juurihakemistossa (ot-harjoitystyo).


1: Asenna riippuvuudet

```bash
poetry install
```

2: Mene virtuaaliympäristöön

```bash
poetry shell
```

3: Suorita aloitustoimenpiteet (tämän tarvitsee tehdä vain kerran)
```bash
poetry run invoke build
```

Nyt kun ohjelma on asennettu, voit käynnistää sen komennolla:

```bash
poetry run invoke start
```

Tästä eteenpäin ohjelma käynnistyy viimeisimmällä komennolla.

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
