# Tietokannan rakenne

## Tietokantakaavio

![](https://github.com/Deemusc/Tsoha-Botnian-tilastosovellus/blob/master/documentation/tietokantakaavio_kuvana.png)

## Tietokantakaavio tekstimuodossa

[Player|(pk)id:Integer;number:Integer;name:String;(fk)teamname:String]

[Game|(pk)id:Integer;date:Date;opponent:String;botnia_goals:Integer;opponent_goals:Integer;(fk)teamname:String]

[Stat|(pk)id:Integer;(fk)game_id:Integer;(fk)player_id:Integer;goals:Integer;assists:Integer;penalties:Integer]

[Account|(pk)id:Integer;name:String;username:String;password:String;teamname:String]

[Stat]*-1[Player]

[Stat]*-1[Game]

[Game]*-1[Account]

[Player]*-[Account]
