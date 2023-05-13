# Käyttöohje

Ohjelmaan tarvitaan vähintään pythonin versio 3.8. Ohjelma on julkaistu poetryn version 1.4.2 kanssa.

Kloonaa [repositorio](https://github.com/thefakejj/Minesweeper) koneellesi. (myöhemmin tähän release)

## Konfigurointi
Voit vaihtaa tietokantatiedoston nimen .env-tiedostossa, jolloin voit esimerkiksi käyttää useampia tulostauluja.
Tiedostot luodaan automaattisesti data-hakemistoon.
.env-tiedostossa tietokantatiedoston nimi määritellään seuraavasti:
```
DATABASE_FILENAME=databasename.db
```

## Ohjelman käynnistäminen

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


## Pelin pelaaminen

Jotta voit pelata peliä, sinun tulee asettaa jokin nimi "Name"-kenttään.
![menu](./kuvat/menu_screenshot.png)

Kun olet valinnut nimen, voit aloittaa pelin klikkaamalla "Play".
![menu_name](./kuvat/menu_name_screenshot.png)


Avaa ensimmäinen ruutu hiiren vasemmalla painikkeella, minkä jälkeen miinat satunnaisesti muodostuvat. Voit liputtaa ruudun oikealla painikkeella.
![game](./kuvat/game_screenshot.png)

Kun klikkaat ruudusta, pelin kello käynnistyy. Pelin sisällä avaamasi ruutu näyttää sitä ympäröivien miinojen määrän. Tyhjä avattu ruutu vastaa nollaa ympäröivää miinaa. Voit palata valikkoon "Back to menu" -nappia painamalla. Peli muistaa nimesi, kun palaat menuun.
![game](./kuvat/game_started_screenshot.png)

Jos paljastat miinan, häviät pelin ja kaikki liputtamattomat miinat paljastuu.
![mine](./kuvat/mine_screenshot.png)

Jos onnisut paljastamaan kaikki miinattomat ruudut, voitat pelin ja kaikki liputtomat miinat paljastuu.
![win](./kuvat/game_win_screenshot.png)


## Tulostaulu

Tulostaulua pääsee katsomaan menusta "Leaderboard"-painikkeesta. Näkymässä näkyy sen vaikeustason tulostaulu, mikä ollaan valittu menussa Field sizella.
![menu_leaderboard](./kuvat/menu_leaderboard_screenshot.png)

Tietyn vaikeustason tulokset näkyvät tulostaulukossa näin:
![leaderboard](./kuvat/leaderboard_screenshot.png)
Takaisin menuun pääsee "Back to menu" -painikkeesta.