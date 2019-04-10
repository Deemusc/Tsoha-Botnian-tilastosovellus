## Pelaajien listaaminen

Pelaajat listataan lisäämisjärjestyksessään linkin *List players* takaa.

## Pelaajan lisääminen tilastotietokantaan

Uusi pelaaja lisätään tilastoihin *Add a player* -linkistä. Pelaajalle syötetään nimi ja pelinumero. Uusi pelajaa lisätään tietokantatauluun **player**.

## Pelaajien haku ja muokkaaminen tai poistaminen

Pelaajia voidaan hakea nimen perusteella linkin *Search players* takaa. Haku löytää pelaajat nimen alun perusteella, yksikin kirjain riittää, eikä kirjainkoolla ole merkitystä. Pelaajaa voidaan muokata joko hakemalla tietty pelaaja hakutoiminnon kautta tai listaamalla kaikki pelaajat. Molemmissa tapauksissa pelaajan vieressä on nappi *Edit player*, josta pääsee syöttämään pelaajalle uudet tiedot. Tiedot päivitetään tietokantatauluun **player**. Pelaaja poistaminen aloitetaan samoin kuin muokkaaminen, hakutoiminnon tai listaamisen kautta. Pelaajan vieressä on nappi *Delete player*, josta pelaajan voi poistaa pysyvästi tietokantataulusta **player**.

## Otteluiden listaaminen

Ottelut voidaan listata lisäämisjärjestyksessään linkin *List games* takaa.

## Ottelun lisääminen tietokantaan

Uusi ottelu lisätään tilastoihin *Add a game* -linkistä. Ottelulle annetaan päivämäärä, vastustajajoukkueen nimi sekä vastustajan tekemien maalien määrä. Uusi ottelu lisätään tietokantatauluun **game**. Seuraavaksi siirrytään sivulle, jossa syötetään Botnian ottelussa pelanneet pelaajat. Sivu listaa kaikki joukkueen pelaajat syöttämisen helpottamiseksi. Pelaajat syötetään yksi kerrallaan pelinumeron perusteella. Eteenpäin siirrytään napilla *finish*. Seuraavaksi päästään syöttämään Botnian ottelussa tekemät maalit. Maalille annetaan maalintekijän numero ja syöttäjän numero. Maali lisätään napista *Add goal*. Uusia maaleja syötetään yksi kerrallaan, kunnes kaikki maalit on syötetty. *Finish*-napilla siirrytään vielä Botnian ottelussa ottamien jäähyjen syöttämiseen. Jäähylle syötetään rangaistuksen kärsijä ja valitaan pudotusvalikosta minuuttimäärä. Lopulta siirrytään otteluiden listaukseen *Finish*-napilla.

## Otteluiden haku ja muokkaaminen tai poistaminen

Otteluita voidaan hakea vastustajan nimen perusteella linkin *Search games* takaa. Haku löytää ottelut haettua vastustajaa vastaan, hakea voi myös joukkueen nimen alun perusteella. Kuten pelaajien muokkaaminen ja poistaminen, otteluidenkin muokkaaminen ja poistaminen aloitetaan hakemalla ottelu tai listaamalla ne kaikki. Ottelun vieressä on nappi *Edit game*, josta pääsee syöttämään ottelulle uudet tiedot. Napista *Delete game* ottelu poistetaan pysyvästi tietokantataulusta **game**.

## Maalipörssin, syöttöpörssin ja pelattujen otteluiden tarkastelu

Linkistä *Goal scorers* löytyvät maalipörssi, syöttöpörssi, ja pelatut ottelut. Toisin sanoen listattuna kaikki maaleja tehneet pelaajat, kaikki syöttöjä antaneet pelaajat ja kaikki otteluissa pelanneet pelaajat. SQL-kyselyssä haetaan taulusta **goal** sarakkeen **scorer_id** esiintymiskertoja, jotka sitten ryhmitellään samaisen sarakkeen mukaan ja järjestetään kertojen mukaisesti laskevasti. Kyselyssä yhdistetään taulu **player** mukaan (scorer_id = player.id), jotta tietty pelaaja voidaan yhdistää maalimääriin. Vastaavasti toimitaan syöttöjen kanssa.
