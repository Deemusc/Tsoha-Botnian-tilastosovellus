# Tietokannan rakenne

## Käsiteanalyysi ja tietokannan rakenteen suunnittelu

Tarkoitus on luoda tilastosovellus salibandyjoukkueelle, johon voidaan tallettaa otteluita, pelaajia ja otteluissa tapahtuvia tilastomerkintöjä. Ottelusta riittää tietää
yksittäisen pelaajan ottelussa tekemät maalit, syötöt ja otetut jäähyminuutit. Käsitteiksi saadaan pelaaja, ottelu ja tilastomerkintä, joka käsittää yhden pelaajan
yhdessä ottelussa keräämät merkinnät. Sovellusta voi käyttää useampi joukkue, mutta joukkueen on tarkoitus nähdä vain oman joukkueensa tilastot, joten tarvitsemme
käsitteen käyttäjä.

Käsitteiden välisiä yhteyksiä ja osallistumisrajoitteita pohtimalla huomataan, että ottelussa voi esiintyä monta pelaajaa ja pelaaja voi pelata useammassa ottelussa.
Toisaalta tilastomerkintä pitää sisällään tiedon sekä ottelusta, jossa merkinnät tehtiin, että pelaajasta, joka ne teki. Ei siis yhdistetä suoraan pelaajaa ja ottelua, vaan
tehdään se tilastomerkinnän kautta. Koska yksi pelaaja voi olla vain kerran yhdessä ottelussa, yhdistelmän ottelusta ja pelaajasta tilastomerkintätaulussa on oltava
uniikki. Käyttäjän tulee olla yhteydessä pelaajaan ja otteluun, jotta käyttäjälle voidaan näyttää vain hänen joukkueensa tilastoja. Jotta samalle joukkueelle voidaan
luoda useampi (eritasoinen) käyttäjä, luodaan tietokantataulu joukkueelle, jota kautta liitetään käyttäjä otteluihin ja pelaajiin.

Pelaajan attribuutteina tulee olla id:n lisäksi pelaajan numero ja nimi. Ottelulle halutaan tallettaa id:n lisäksi päivämäärä, vastustajajoukkueen nimi ja molempien 
joukkueiden tekemien maalien määrä. Kuvataan tilastomerkintöjä taululla *Stat*, johon yhdistetään pelaajan ja ottelun id, sekä näihin liittyen maalien, syöttöjen ja 
jäähyminuuttien määrä. Käyttäjälle annetaan attribuuteiksi joukkueen nimi, käyttäjänimi ja salasana.

## Tietokantakaavio

![](https://github.com/Deemusc/Tsoha-Botnian-tilastosovellus/blob/master/documentation/tietokantakaavio_kuva.png)

## Tietokantakaavio tekstimuodossa

[Player|(pk)id:Integer;number:Integer;name:String;(fk)team_id:Integer]

[Game|(pk)id:Integer;date:Date;opponent:String;our_goals:Integer;opponent_goals:Integer;(fk)team_id:Integer]

[Stat|(pk)id:Integer;(fk)game_id:Integer;(fk)player_id:Integer;goals:Integer;assists:Integer;penalties:Integer]

[Team|(pk)id:Integer;name:String]

[Account|(pk)id:Integer;username:String;password:String;(fk)team_id:Integer]

[Stat]*-1[Player]

[Stat]*-1[Game]

[Game]*-1[Team]

[Player]*-1[Team]

[Team]1-*[Account]

## Create table -lauseet

**Käyttäjä-taulun luonti**

CREATE TABLE account (

	id INTEGER NOT NULL, 

	username VARCHAR(32) NOT NULL, 

	password VARCHAR(32) NOT NULL, 

	role VARCHAR(10) NOT NULL, 

	team_id INTEGER NOT NULL, 

	PRIMARY KEY (id), 

	FOREIGN KEY(team_id) REFERENCES team (id)

);

**Joukkue-taulun luonti**

CREATE TABLE team (

	id INTEGER NOT NULL, 

	name VARCHAR(32) NOT NULL, 

	PRIMARY KEY (id), 

	UNIQUE (name)

);

**Pelaaja-taulun luonti**

CREATE TABLE player (

	id INTEGER NOT NULL, 

	number INTEGER NOT NULL, 

	name VARCHAR(48) NOT NULL, 

	team_id INTEGER NOT NULL, 

	PRIMARY KEY (id), 

	FOREIGN KEY(team_id) REFERENCES team (id)

);

**Ottelu-taulun luonti**

CREATE TABLE game (

	id INTEGER NOT NULL, 

	date DATE NOT NULL, 

	opponent VARCHAR(32) NOT NULL, 

	our_goals INTEGER NOT NULL, 

	opponent_goals INTEGER NOT NULL, 

	team_id INTEGER NOT NULL, 

	PRIMARY KEY (id), 

	FOREIGN KEY(team_id) REFERENCES team (id)

);

**Tilasto-taulun luonti**

CREATE TABLE stat (

	id INTEGER NOT NULL, 

	game_id INTEGER NOT NULL, 

	player_id INTEGER NOT NULL, 

	goals INTEGER NOT NULL, 

	assists INTEGER NOT NULL, 

	penalties INTEGER NOT NULL, 

	PRIMARY KEY (id), 

	CONSTRAINT unique_game_player UNIQUE (game_id, player_id), 

	FOREIGN KEY(game_id) REFERENCES game (id), 

	FOREIGN KEY(player_id) REFERENCES player (id)

);
