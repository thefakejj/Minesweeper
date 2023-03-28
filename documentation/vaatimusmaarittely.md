# Vaatimusmäärittely

## Miinaharava

Sovellus alkaa valikosta, mistä käyttäjä voi aloittaa pelin, muuttaa asetuksia, katsoa tuostaulua tai sulkea sovelluksen.


### Peli

- Sovellus muodostaa satunnaisen kentän
- Sovellus käynnistää pelin alkaessa sekuntikellon
- Käyttäjän tavoite on paljastaa kaikki ruudut, joissa ei ole miinaa
    - Jos käyttäjä paljastaa miinan, käyttäjä häviää pelin
- Paljastetulla ruudulla lukee numero, joka kertoo, kuinka monta miinaa löytyy sen ympäröivistä kahdeksasta ruudusta
- Käyttäjä voi liputtaa ruudun, ja poistaa ruudun liputuksen
    - Liputettua ruutua ei voi paljastaa
- Jos käyttäjä paljastaa kaikki miinattomat ruudut, käyttäjä voittaa pelin

### Tulostaulu

- Kun pelaaja läpäisee pelin, häneltä kysytään nimeä, joka ajan kanssa lisätään tulostauluun
- Tulostaulu tallentuu paikallisesti

### Asetukset

- Pelin ruudukon väriä pystyy muuttamaan
- Voi valita ruudukon koon

