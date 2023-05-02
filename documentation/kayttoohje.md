# Käyttöohje

Lataa [viimeisimmän releasen](https://github.com/thefakejj/ot-harjoitustyo/releases/tag/viikko6) lähdekoodi tai kloonaa vaikka [repositorio](https://github.com/thefakejj/ot-harjoitustyo) koneellesi.

## Ohjelman käynnistäminen

1: Mene virtuaaliympäristöön

```bash
poetry shell
```

2: Asenna riippuvuudet

```bash
poetry install
```

3: Nyt kun ohjelma on asennettu, voit käynnistää sen komennolla:

```bash
poetry run invoke start
```


## Pelin pelaaminen

Valitse klikkailemalla ruudukon koko ja paina "Play"
![menu](./kuvat/menu_screenshot.png)


Avaa ensimmäinen ruutu hiiren vasemmalla painikkeella, minkä jälkeen miinat satunnaisesti muodostuvat. Voit liputtaa ruudun oikealla painikkeella. Pelin sisällä avaamasi ruutu näyttää sitä ympäröivien miinojen määrän. Tyhjä avattu ruutu vastaa nollaa ympäröivää miinaa. Voit palata valikkoon "Back to menu" -nappia painamalla.
![game](./kuvat/game_screenshot.png)

Paljastettu miina näyttää tältä. Olehan varovainen!

![mine](./kuvat/mine_screenshot.png)