# Käyttötapaukset ja SQL-kyselyt

## Pelaajien listaaminen

Pelaajat listataan lisäämisjärjestyksessään linkin *List players* takaa. Käyttäjälle listataan vain hänen joukkueensa pelaajat.

**SQL-kysely**:
```SQL
SELECT * FROM Player 
WHERE team_id=?;
```

## Pelaajan lisääminen tilastotietokantaan

Uusi pelaaja lisätään tilastoihin *Add a player* -linkistä. Pelaajalle syötetään nimi ja pelinumero. Pelaajalle annetaan joukkueeksi käyttäjän joukkue.

**SQL-kysely**:
```SQL
INSERT INTO Player (number, name, team_id) 
VALUES (?, ?, ?);
```

## Pelaajien haku ja muokkaaminen tai poistaminen

Pelaajia voidaan hakea nimen perusteella linkin *Search players* takaa. Haku löytää pelaajat nimen alun perusteella, yksikin kirjain riittää, eikä kirjainkoolla ole merkitystä.
Käyttäjä voi hakea vain oman joukkueensa pelaajia.

**SQL-kysely**: 
```SQL
SELECT * FROM Player 
WHERE team_id=? AND name LIKE '?%';
```

Pelaajaa voidaan muokata joko hakemalla tietty pelaaja hakutoiminnon kautta tai listaamalla kaikki pelaajat. Molemmissa tapauksissa pelaajan vieressä on nappi *Edit player*, josta pääsee syöttämään pelaajalle uudet tiedot.

**SQL-kysely**: 
```SQL
UPDATE Player SET number=?, name=? 
WHERE id=?;
```

Pelaajan poistaminen aloitetaan samoin kuin muokkaaminen, hakutoiminnon tai listaamisen kautta. Pelaajan vieressä on nappi *Delete player*, josta pelaajan voi poistaa.

**SQL-kysely**: 
```SQL
DELETE FROM Player 
WHERE id=?;
```

## Otteluiden listaaminen

Ottelut voidaan listata lisäämisjärjestyksessään linkin *List games* takaa. Käyttäjälle listataan vain hänen joukkueensa ottelut.

**SQL-kysely**: 
```SQL
SELECT * FROM Game 
WHERE team_id=?;
``` 

## Ottelun lisääminen tietokantaan

Uusi ottelu lisätään tilastoihin *Add a game* -linkistä. Ottelulle annetaan päivämäärä, vastustajajoukkueen nimi sekä joukkueiden tekemien maalien määrät.
Lisäksi ottelun joukkueeksi lisätään käyttäjän joukkue.

**SQL-kysely**: 
```SQL
INSERT INTO Game (date, opponent, botnia_goals, opponent_goals, team_id) 
VALUES (?, ?, ?, ?, ?);
```

Seuraavaksi siirrytään sivulle, jossa syötetään Botnian pelaajien tilastot ottelussa. 

**SQL-kysely**: 
```SQL
INSERT INTO Stat (game_id, player_id, goals, assists, penalties) 
VALUES (?, ?, ?, ?);
```

## Otteluiden haku ja muokkaaminen tai poistaminen

Otteluita voidaan hakea vastustajan nimen perusteella linkin *Search games* takaa. Haku löytää ottelut haettua vastustajaa vastaan, hakea voi myös joukkueen nimen alun perusteella.
Käyttäjä voi hakea vain oman joukkueensa otteluita.

**SQL-kysely**: 
```SQL
SELECT * FROM 
WHERE team_id=? AND opponent LIKE '?%';
```

Kuten pelaajien muokkaaminen ja poistaminen, otteluidenkin muokkaaminen ja poistaminen aloitetaan hakemalla ottelu tai listaamalla ne kaikki. Ottelun vieressä on nappi *Edit game*, josta pääsee syöttämään ottelulle uudet tiedot.

**SQL-kysely**: 
```SQL
UPDATE Game SET date=?, opponent=?, botnia_goals=?, opponent_goals=? 
WHERE id=?;
```

Napista *Delete game* ottelu poistetaan.

**SQL-kysely**: 
```SQL
DELETE FROM Game 
WHERE id=?;
```

Samalla tulee luonnollisesti poistaa tilastomerkinnät ottelusta.

**SQL-kysely**: 
```SQL
DELETE FROM Stat 
WHERE game_id = ?;
```

## Ottelun yksityiskohtien tarkastelu

Otteluiden listauksen tai haun yhteydessä ottelun vieressä on nappi *Details*, josta päästään tarkastelemaan kyseisen ottelun tilastomerkintöjä.

**SQL-kysely**: 
```SQL
SELECT number, name, goals, assists, penalties FROM Player 
JOIN Stat ON Stat.player_id=Player.id 
WHERE Stat.game_id=?;
```

## Pistepörssin tarkastelu

Linkistä *Statistics* päästään tarkastelemaan Botnian pistepörssiä, eli pelaajien pelattuja otteluita, maaleja, syöttöjä, pisteitä ja jäähyminuutteja.

**SQL-kysely**: 
```SQL
SELECT Player.number, Player.name, COUNT(Stat.player_id) AS games, 
SUM(Stat.goals) AS goals,
SUM(Stat.assists) AS assists, 
SUM(goals + assists) AS points, 
SUM(Stat.penalties) AS penalties FROM Player 
LEFT JOIN Stat ON Stat.player_id=Player.id 
WHERE Player.team_id=?
GROUP BY Player.id
ORDER BY points DESC, goals DESC, penalties;
```
