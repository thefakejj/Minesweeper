# Arkkitehtuurikuvaus

## Rakenne
Pelin pakkausrakenne on seuraava:

![Pakkauskaavio](./kuvat/pakkausdiagrammi.png)

Ui sisältää pelin käyttöliittymän, menun, käyttäjän syötteet ja loopin. Services sisältää pelin logiikan koodia. Enums sisältää enumerateja, joilla selkeytetään koodia. Repositories-hakemistossa taas on tietokannan rajapinnan koodia.

## Käyttöliittymä

Käyttöliittymä sisältää kaksi eri näkymää: asetukset, tulostaulun ja pelin. Ruudulla on kerrallaan aina yksi näkymä. Pygame-menulla on oma looppinsa, mutta se käyttää minesweeper-olion ikkunaa. Pygamen loopissa kutsutaan Renderer-luokkaa, joka piirtää näytön.

Kun käyttäjä painaa menussa play, kutsutaan Minesweeper-luokan go_to_game -funktiota, joka vie käyttäjän peliin. Jos menussa painaa leaderboard, kutsutaan Minesweeper-luokan go_to_leaderboard -funktiota. Kummankin näkymän sisällä taas voi painaa nappia "back to menu", joka vie käyttäjän takaisin menuun.

## Pelin logiikka

Ohjelmassa annetaan ui:n Menu- ja Minesweeper -luokilta saatuja käyttäjän interaktiosta muodostuvia syötteitä servicesin luokille Grid, Field ja Clock.

### Luokkakaavio

![Luokkakaavio](./kuvat/luokkakaavio.png)

Ensin luodaan minesweeper-olio, jonka displayn päälle Menu laittaa oman displaynsä. Menu-luokasta kutsutaan Minesweeper-luokan metodeja. Minesweeper-luokka käyttää kaikkia kaaviossa oikealla olevia luokkia. Luokka MouseEvent käyttää luokista Grid ja Field olioita, mutta se saa ne Minesweeper-luokan kautta injektiona. Luokka Grid myös käyttää samoin Field-oliota ja saa sen Minesweeper-luokalta.

Luokka Field esimerkiksi muodostaa MouseEventistä klikkikoordinaatin avulla satunnaisen miinaruudukon, jossa klikattu ruutu ei saa olla miina.

Luokka Grid taas saa päivittää näkyvältä ruudukolta MouseEventin antaman ruudun vastaamaan käyttäjän syötettä (vasen/oikea klikkaus, avaus/liputus) ja ruutua ympäröivien miinojen määrää.

Luokka Clock vastaa sekä pelin sekuntikellosta että fps:n asettamisesta. Luokan metodit ylläpitää pelin alkuaikaa, pelin nykyistä aikaa, pelin loppuaikaa ja laskee kuluneen ajan sekä läpäisemisen menneen ajan. Minesweeper-luokka kutsuu Clockin metodeja päästäkseen käsiksi aikoihin.

Luokka Leaderboard tallentaa ajat tulostauluihin. Minesweeper kutsuu Leaderboardia ja Clockia, ja tallentaa nimen ja ajan tietokantaan.

<br>

## Tiedon pysyväistallennus

Luokka Leaderboard tallentaa tietoa SQLite-tietokantaan.

Juurihakemistosta löytyy konfiguraatiotiedosto [.env](https://github.com/thefakejj/Minesweeper/blob/main/.env), jossa voidaan määritellä tiedostonimi, johon tulokset tallennetaan.

Ajat on taulussa muodossa (nimi TEXT, aika FLOAT).

Tiedot tallennetaan miinaharavan vaikeustasoihin jaettuihin tauluihin _8x8, _16x6 ja _24x16 tietokannassa, joka alustetaan [initialize_database.py](https://github.com/thefakejj/Minesweeper/blob/main/src/initialize_database.py)-tiedostossa.

<br>

## Keskeiset toiminnallisuudet
Tässä osassa on pelin ohjelman toimintaa kuvaavia yksinkertaistettuja sekvenssikaavioita. Jotkin sekvenssikaaviot ovat melko pitkiä, koska funktioihin injektoidaan monia asioita.

### Pelin avaus

#### Avaus alustaa pygamen ja antaa Minesweeperille kaikki oletusarvot


```mermaid
sequenceDiagram

  Index->>Minesweeper: Minesweeper()
  Minesweeper->>Minesweeper: window-width, window_height
  Minesweeper->>Minesweeper: grid_width = 8, grid_height = 8
  Minesweeper->>Minesweeper: bg_color = (128, 255, 128)
  Minesweeper->>Minesweeper: player_name = ""
  Minesweeper->>Minesweeper: first_click_has_happened = False
  Minesweeper->>Minesweeper: game_state = 0
  Minesweeper->>Minesweeper: x_where_grid_ends = 0

  Minesweeper->>Clock: Clock()
  Minesweeper->>Leaderboard: Leaderboard()
  
  Minesweeper->>Minesweeper: surface
  Minesweeper->>Minesweeper: run_menu()
  
  Minesweeper->>Menu: Menu(go_to_game, set_minesweeper_size, surface, set_player_name, player_name, go_to_leaderboard)

  Minesweeper->>Menu: menu.menu()
  Menu->>Menu: menu.mainloop(surface)

```
<br>

### Peliin meneminen

#### Käytetään esimerkkinä tilannetta, missä pelajaa valitsee ruudukon kooksi 8x8

```mermaid
sequenceDiagram
  actor Player input

  Player input->>Menu: Field size: 8x8
  Player input->>Menu: Play
  Menu->>Minesweeper: go_to_game()
  Minesweeper->>Minesweeper: change_game_state(1)
  Minesweeper->>Minesweeper: change_view()

  Minesweeper->>Field: Field(grid_width, grid_height)
  Minesweeper->>Grid: Grid(grid_width, grid_height)
  Minesweeper->>Scaling: Scaling(window_height, DEFAULT_IMAGE_SIZE, grid_width, grid_height)
  Minesweeper->>Scaling: get_grid_edge_x_coordinates()
  Scaling-->>Minesweeper: x_where_grid_ends
  Minesweeper->>Scaling: get_scaled_image_size()
  Scaling-->>Minesweeper: image_size
  Minesweeper->>Images: Images(image_size)
  Images-->>Minesweeper: images, buttons
  Minesweeper->>MouseEvent: MouseEvent(image_size, grid_width, grid_height, x_where_grid_ends, change_game_state)
  Minesweeper->>Renderer: Renderer(images, buttons, image_size)
  Minesweeper->>Minesweeper: main_loop()

```
<br>


### Ensimmäinen klikkaus

#### Pelaajan ensimmäinen klikkaus ruudukossa, joka muodostaa backissa miinaruudukon listana. Tässä vaiheessa ruudukon koko on jo valittu, ja se on Minesweeper-oliolla muistissa.


```mermaid
sequenceDiagram
  actor Player input
  
  Minesweeper->>Minesweeper: main_loop()
  Player input->>Minesweeper: event_checker(click_x_position, click_y_position)
  Minesweeper->>MouseEvent: square_click(click_coordinates)
  MouseEvent->>MouseEvent: which_square_was_clicked(click_coordinates)
  MouseEvent-->>MouseEvent: return square_coordinates
  MouseEvent->>Minesweeper: change_game_state(2)
  MouseEvent->>Minesweeper: start_game(square_coordinates)
  Minesweeper->>Field: create_random_field(square_coordinates)
  Field-->>Minesweeper: real_field
  Minesweeper->>Clock: set_start_time()
  Clock->>Clock: _start_time = get_ticks()

```
<br>

### Ruudukon päivittäminen

#### Tilanne, jossa miinojen sijainnit on jo generoitu, ruutua ei ole avattu ja ruutu ei ole miina.

```mermaid
sequenceDiagram
  actor Player input
  
  Minesweeper->>Minesweeper: main_loop()
  Player input->>Minesweeper: event_checker(click_x_position, click_y_position)
  Minesweeper->>MouseEvent: square_click(click_coordinates)
  MouseEvent->>MouseEvent: which_square_was_clicked(click_coordinates)
  MouseEvent-->>MouseEvent: return square_coordinates
  MouseEvent->>Grid: update_grid(square_coordinates, event_button, field_grid)
  Grid->>Grid: count_nearby_mines(square_coordinates, field_grid)
  Grid-->>Grid: nearby_mines
  Grid->>Grid: revealed_tiles += 1
  Grid->>Grid: set_square_content(square_coordinates, 3 + nearby_mines)
  Minesweeper->>Renderer: render()
  Renderer->>Renderer: draw_grid()
  Minesweeper->>Minesweeper: pygame.display.flip()
```
<br>

### Pelin voittaminen, tuloksen tallentaminen

#### Tilanne, jossa pelaaja voittaa pelin

```mermaid
sequenceDiagram
  actor Player input

  Player input->>Menu: Name: name
  Menu->>Minesweeper: set_player_name(name)
  Minesweeper-->>Minesweeper: player_name = name
  Player input->>Menu: Play
  Menu->>Minesweeper: go_to_game()
  Minesweeper->>Minesweeper: change_game_state(1)
  Minesweeper->>Minesweeper: change_view()
  
  Minesweeper->>Minesweeper: main_loop()
  Player input->>Minesweeper: event_checker(click_x_position, click_y_position)
  Minesweeper->Minesweeper: last square flipped
  Minesweeper->>Grid: check_if_enough_squares_flipped()
  Grid->>Minesweeper: True
  Minesweeper->>Minesweeper: change_game_state(4)
  Minesweeper->>Clock: set_stop_time()
  Clock->>Clock: _stop_time = get_ticks()
  Minesweeper->>Clock: set_finish_time()
  Clock->>Clock: _finish_time = get_stop_time() - get_start_time()
  Minesweeper->>Grid: reveal_grid(field_grid)
  Grid->>Grid: loops through grid
  Grid->>Grid: update_grid
  Minesweeper->>Clock: get_finish_time_in_seconds()
  Clock-->>Minesweeper: finish_time
  Minesweeper->>Leaderboard: insert_time((grid_width, grid_height), player_name, finish_time)
  Minesweeper->>Minesweeper: game_state = 4
  Minesweeper->>Renderer: render()
  Renderer->>Renderer: draw_grid()
  Minesweeper->>Minesweeper: pygame.display.flip()
```
<br>

### Pelaaja menee tulostauluun

```mermaid
sequenceDiagram
  actor Player input
  
  Player input->>Menu: Leaderboard
  Menu->>Minesweeper: go_to_leaderboard
  Minesweeper->>Minesweeper: change_game_state(5)
  Minesweeper->>Minesweeper: change_view()

  Minesweeper->>Minesweeper: main_loop()
  Minesweeper->>Renderer: render()
  Renderer->>Renderer: draw_leaderboard()
  Renderer->>Leaderboard: grid_leaderboard(grid_width, grid_height)
  Leaderboard-->>Renderer: table
  Minesweeper->>Minesweeper: pygame.display.flip()
```
<br>


## Ohjelman rakenteeseen jääneet heikkoudet

Ohjelmassa on käyttöliittymää ja logiikkaa sekaisin, mikä esimerkiksi aiheuttaa tarpeen koodin toistolle, jotta testejä voidaan pyörittää.