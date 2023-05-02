# Arkkitehtuurikuvaus

## Rakenne
Pelin pakkausrakenne on seuraava:

![Pakkauskaavio](./kuvat/pakkausdiagrammi.png)

Services sisältää pelin logiigan koodia, ui sisältää käyttöliittymän koodia ja menu sisältää pygame-menun koodin. Assets sisältää pelissä tarvittavia kuvia. Enums sisältää enumerateja, joilla selkeytetään koodia. Repositories-hakemistossa taas on tietokannan ja sovelluksen rajapinnan koodia.

## Käyttöliittymä

Käyttöliittymä sisältää kaksi eri näkymää: asetukset ja pelin. Vaikka ui on erillinen hakemisto, vastaa se oikeastaan vain pelin piirtämisestä. Pygame-menu -kirjastolla on oma piirtometodinsa, joka käyttää minesweeperin ikkunaa. Tämä metodi sijaitsee Menu-luokassa.

Kun käyttäjä painaa menussa play, kutsutaan Minesweeper-luokan go_to_game -funktiota, joka vie käyttäjän peliin. Pelin sisällä taas voi painaa nappia "back to menu", joka vie käyttäjän takaisin menuun.

## Sovelluslogiikka

### Luokkakaavio

![Luokkakaavio](./kuvat/Minesweeper_luokkakaavio.png)


### Sekvenssikaavio

#### Pelaajan ensimmäinen klikkaus ruudukossa (Kaavio ei ole täydellisen kuvaava tilanteesta, mutta siinä kuitenkin tulee ilmi, mitä luokkia, metodeja ja muuttujia käytetään missäkin, ja miten muuttujat siirretään)
```mermaid
sequenceDiagram
  actor Player input
  participant Minesweeper
  participant ClickChecker
  participant Field
  
  
  Player input->>Minesweeper: event_checker(click_x_position, click_y_position)
  Minesweeper->>ClickChecker: square_click(click_coordinates)
  ClickChecker->>ClickChecker: which_square_was_clicked(click_coordinates)
  ClickChecker-->>ClickChecker: square_coordinates
  ClickChecker->>Minesweeper: start_game(square_coordinates)
  Minesweeper->>Field: __init__(square_coordinates)
  Field->>Field: create_random_field(square_coordinates)

```

