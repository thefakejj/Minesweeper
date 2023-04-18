# Miinaharava

Miinaharava on muun muassa vanhoista Windows-versioista tuttu peli *Minesweeper*. Pelin tavoitteena on paljastaa kaikki ruudut, joiden alla ei ole miinaa. Jos paljastaa miinan, häviää pelin. Pelissä pystyy myös liputtamaan miinaksi epäiltyjä ruutuja.


## Dokumentaatio

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