# Sovelluksen asennus- ja käyttöohje

## Asennusohje

### Asentaminen paikallisesti

Kloonaa repositorio käyttöösi ja siirry juurikansioon.

Luo virtuaaliympäristö ```venv``` komennolla:

```python3 -m venv venv```

Ota virtuaaliympäristö käyttöön komennolla:

```source venv/bin/activate```

Asenna riippuvuudet komennolla:

```pip install -r requirements.txt```

Aja sovellus komennolla:

```python run.py```

### Asentaminen Herokuun

Tarvitset käyttäjätilin Herokuun.

Luo sovellukselle paikka Herokuun komennolla:

```heroku create Sovelluksesi-nimi```

Lisää tieto Herokusta git:iin komennolla:

```git remote add heroku https://git.heroku.com/Sovelluksesi-nimi.git```

Lisää ohjelman koodi Herokuun komennolla: 

```git add . git commit -m "Commit-viestisi" git push heroku master```

Lisää sovelluksen käyttöön tieto Herokusta komennolla:

```heroku config:set HEROKU=1```

Luo tietokanta Herokuun komennolla:

```heroku addons:add heroku-postgresql:hobby-dev```

## Käyttöohje

Sovelluksessa on kahdentyyppisiä käyttäjiä, admin- ja peruskäyttäjät. Admin-käyttäjä voi käyttää kaikkia sovelluksen toiminnallisuuksia ja peruskäyttäjä voi listata 
pelaajia ja otteluita, hakea niitä, sekä tarkastella tilastoja. Admin-käyttäjä voi myös luoda uusia peruskäyttäjiä joukkueelleen.

### Kirjautuminen ja uuden tunnuksen luominen

Sovellukseen kirjaudutaan sisään oikean reunan *Log in* -painikkeesta. Viereisestä *Sign up* -painikkeesta voi luoda uuden admin-käyttäjän uudelle joukkueelle. Samassa 
kohdassa lukee sisäänkirjautuneen käyttäjän nimi ja on mahdollisuus kirjautua ulos. Sisäänkirjautuneena oikealla on myös linkki *Create new regular user*, josta
admin-käyttäjä voi luoda joukkueelle uuden peruskäyttäjän.

### Pelaajaan liittyvät toiminnallisuudet

Koska tilastoja lasketaan pelaajille, on suositeltavaa lisätä pelaajia ennen muita toimintoja. Pelaajan lisääminen onnistuu painikkeesta *Add player*. Pelaajalle syötetään pelinumero, joka ei saa 
olla jo joukkueen pelaajalla käytössä, ja nimi. Painikkeesta *List players* pääsee tarkastelemaan pelaajia. Pelaajia voi muokata listausnäkymässä pelaajan viereen 
tulevasta painikkeesta *Edit*. Muokkaustila toimii pelaajan lisäämistilan tavoin. Pelaajan voi myös poistaa samasta näkymästä *Delete*-painikkeesta.

Pelaajia voi myös hakea nimen perusteella *Search players* -painikkeesta. Haku löytää kaikki pelaajat, joiden nimen alussa on haettu kirjainyhdistelmä.

### Otteluihin liittyvät toiminnallisuudet

Uusi ottelu lisätään *Add game* -painikkeesta. Ottelulle syötetään ensin päivämäärä, vastustajajoukkueen nimi, oman joukkueen tekemien maalien määrä, sekä 
vastustajajoukkueen tekemien maalien määrä. Siirryttäessä eteenpäin *Add game* -painikkeella, päästään syöttämään joukkueen pelaajien tilastot kyseisessä ottelussa. 
Pudotusvalikosta valitaan pelaaja ja hänelle syötetään ottelussa tehtyjen maalien ja syöttöjen määrät sekä jäähyminuuttien määrä. *Add statistics* -napista lisätään 
pelaajan tiedot järjestelmään. Pelaajan tiedot voidaan syöttää vain kerran yhteen otteluun. Syötä tiedot kaikille otteluissa pelanneille pelaajille, vaikka pelaaja ei olisi
kerännyt tilastomerkintöjä ottelussa (0+0, 0 min). Näin pelaajalle merkataan kuitenkin yksi pelattu ottelu.

Ottelut voidaan listata *List games* -painikkeesta. Otteluita voidaan myös hakea vastaavasti kuin pelaajia, hakukriteerinä annetaan vastustajajoukkueen nimi tai kirjaimia 
nimen alusta. Otteluita voidaan muokata listauksessa ottelun vierestä löytyvällä *Edit*-painikkeella. Ottelusta voidaan muokata perustietoja, päivämäärää, vastustajan nimeä ja
maalimääriä. Mikäli pelaajien tilastot on syötetty väärin, kannattaa ottelu poistaa ja syöttää uudestaan. Ottelu voidaan poistaa *Delete*-painikkeella.

### Tilastojen tarkastelu

Painikkeesta *Statistics* päästään tarkastelemaan tilastoja. Sivu listaa käytännössä joukkueen pistepörssin, eli pelaajien pelaamat ottelut, tehdyt maalit, syötöt, pisteet 
sekä jäähyminuutit.
