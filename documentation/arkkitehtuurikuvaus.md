# Arkkitehtuurikuvaus

## Rakenne
Pelin pakkausrakenne on seuraava:
![Pakkauskaavio](./kuvat/pakkausdiagrammi.png)

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

