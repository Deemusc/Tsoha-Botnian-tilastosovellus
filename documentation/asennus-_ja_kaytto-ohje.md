# Sovelluksen asennus- ja käyttöohje

## Asennusohje

Sovellus toimii Herokun palvelimella Internetissä. Se on käytettävissä selaimella, eikä vaadi erityisiä toimenpiteitä.

## Käyttöohje

Sovelluksessa on kahdentyyppisiä käyttäjiä, admin- ja peruskäyttäjät. Admin-käyttäjä voi käyttää kaikkia sovelluksen toiminnallisuuksia ja peruskäyttäjä voi listata pelaajia ja otteluita, hakea niitä sekä tarkastella tilastoja.

### Kirjautuminen ja uuden tunnuksen luominen

Sovellukseen kirjaudutaan sisään oikean reunan *Log in* -painikkeesta. Viereisestä *Sign up* -painikkeesta voi luoda uuden peruskäyttäjän. Samassa kohtaa lukee sisäänkirjautuneen käyttäjän nimi ja on mahdollisuus kirjautua ulos.

### Pelaajaan liittyvät toiminnallisuudet

Sovellukseen kannattaa lisätä pelaajia ennen muita toimintoja. Pelaajan lisääminen onnistuu painikkeesta *Add player*. Pelaajalle syötetään pelinumero, joka ei saa olla jo käytössä, ja nimi. Painikkeesta *List players* pääsee tarkastelemaan pelaajia. Pelaajia voi muokata listausnäkymässä pelaajan viereen tulevasta painikkeesta *Edit*. Muokkaustila toimii pelaajan lisäämistilan tavoin. Pelaajan voi myös poistaa samasta näkymästä *Delete*-painikkeesta.

Pelaajia voi myös hakea nimen perusteella *Search players* -painikkeesta. Haku löytää kaikki pelaajat, joiden nimen alussa on haettu kirjainyhdistelmä.

### Otteluihin liittyvät toiminnallisuudet

Uusi ottelu lisätään *Add game* -painikkeesta. Ottelulle syötetään ensin päivämäärä, vastustajajoukkueen nimi, Botnian tekemien maalien määrä sekä vastustajajoukkueen tekemien maalien määrä. Siirryttäessä eteenpäin *Add game* -painikkeella, päästään syöttämään Botnian pelaajien tilastot kyseisessä ottelussa. Pudotusvalikosta valitaan pelaaja ja hänelle syötetään ottelussa tehtyjen maalien ja syöttöjen määrät sekä jäähyminuuttien määrä. *Add statistics* -napista lisätään pelaajan tiedot järjestelmään. Pelaajan tiedot voidaan syöttää vain kerran yhteen otteluun.

Ottelut voidaan listata *List games* -painikkeesta. Otteluita voidaan myös hakea vastaavasti kuin pelaajia, hakukriteerinä annetaan vastustajajoukkueen nimi tai kirjaimia alusta. Otteluita voidaan muokata listauksessa ottelun vierestä löytyvällä *Edit*-painikkeella. Ottelun perustietoja voidaan muokata **ja myöhemmin tarkoitus olisi pystyä muokkaamaan myös pelaajien tilastoja ko. ottelussa**. Ottelu voidaan myös poistaa *Delete*-painikkeella.

### Tilastojen tarkastelu

Painikkeesta *Statistics* päästään tarkastelemaan tilastoja. Sivu listaa käytännössä Botnian pistepörssin, eli pelaajien pelaamat ottelut, tehdyt maalit, syötöt, pisteet sekä jäähyminuutit.
