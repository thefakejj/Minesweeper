# Minesweeper-projektin changelog

## Viikko 3

- Lisätty Field-luokka, jonka konstruktori saa syötteen pääohjelmassa ja tekee sen kokoisen, satunnaisen miinaharavaruudukon.
- Lisätty testit luokan metodeille. Testit testaavat, että olio muodostuu, että sen luoman ruudukon korkeus ja leveys on oikea, ja että sen str-esitys on oikea.

## Viikko 4

- Lisätty avautuva ikkuna ja menu. 
    - Menussa voi valita ruudukon koon, sulkea peli tai avata peli. Pelin avaaminen avaa ikkunan, jossa on ruudukko skaalattuna.
    - Ruudukko voi nyt olla epäsymmetrinen
- Ensimmäiseen ruutuun klikkaaminen antaa pelille tiedon, mihin ruutuun ei saa laittaa miinaa.

## Viikko 5

- Erotettu pelin logiikka ja käyttöliittymä eri moduuleihin
    - Tämän yhteydessä on lisätty useita luokkia (jotkin luokat ovat väliaikaisesti tyhjiä)

- Käyttäjä voi peliin menemisen jälkeen liputtaa ruutuja
    - Liputettuja ruutuja ei voi avata (avaamisen toiminta puuttuu, mutta liputettuun ruutuun klikkaaminen ei aiheuta "ensimmäisen klikkauksen" toteutumista)

- Testausta tehty Minesweeper, ClickChecker ja Field -luokille

- Luotu constants-moduuli
    - DEFAULT_IMAGE_SIZE
    - DEFAULT_SIDE_BUTTON_SIZE
    - DEFAULT_WINDOW_WIDTH
    - DEFAULT_WINDOW_HEIGHT

## Viikko 6

- Lisätty miinojen avaaminen peliin
    - Jos miinan avaa, ei voi enää avata lisää ruutuja, vaan joutuu aloittamaan uudestaan
- Lisätty numerot, jotka kertovat ruutua ympäröivien miinojen määrän
- Lisätty back to menu nappi peliin
- Äskeisen kahden kohdan grafiikat luotu

- Lisätty enums, joita käytetään klikkien ja käyttöliittymän kanssa

- Lisätty docstring

- Lisätty testejä ja dokumentaatiota

## Viikko 7

- github-repositorion nimi on nyt Minesweper, ja poetry-projektin nimi on nyt minesweeper
 - Samalla shellin nimi muuttuu

- Lisätty mahdollisuus "voittaa" tai "hävitä" peli
- Lisätty leaderboard
- renderer-luokassa uudet metodid draw_text, draw_leaderboard
- Samalla menussa input-kenttä, johon laitetaan nimi
- peli paljastaa koko kentän, jos voittaa
 - tähän tehty metodi nykyiseen Gridiin

- lisätty ympäristömuuttuja .env ja testiympäristömuuttuja .env.test
 - näiden avulla config.py:n kautta määritellään tietokantatiedoston nimi ja tiedostosijainti
 - samalla tämä päivitetty ohjelman tietokantaosuuteen
 - tietokannalle lisätty testit

- game.py ja mouse_event.py siirretty ui:hi
 - Minesweeper-luokan kellometodit siirretty Clock-luokkaan
  - elapsed time nollaantuu, kun mennään pelinäkymään
  - Testit tehty Clockille
 - Luotu change_view-metodi Minesweeperille, jolla päästään sekä pelinäkymään että tulostauluun
 - MouseEvent ei injektoi enää koko minesweeperia, ja sen metodit injektoivat vain tiettyjä asioita

- UiGridin sijasta on Grid, joka ylläpitää näkyvää gridiä
 - Tässä luokassa on myös entisen check_if_mine.py-tiedoston koodia
 - Testit tehty Gridille

- menu.py siirretty ui:hin

- Poistettu Minesweeperin ja MouseEventin testaus
 - MouseEvent on gridin kanssa testeissä mukana

- Jos poetry run invoke start tulostaa terminaaliin ohjeen ajaa build, jos tietokantaa ei ole alustettu


- Luotu testit constantseille
- Poistettu testauksesta index.py ja enumit

- Laajennettu arkkitehtuurikuvausta 
 - Luotu sekvenssikaavioita keskeisistä toiminnoista
- Luotu testausdokumentaatio
- Päivitetty vaatimusmäärittelyä
- Päivitetty docstring
- Päivitetty readme
- Päivitetty käyttöohjetta
- Tehty release
- Lisätty sallitut merkit menun nimi-inputtiin
- Uusittu release
