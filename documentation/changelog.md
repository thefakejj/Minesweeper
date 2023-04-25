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