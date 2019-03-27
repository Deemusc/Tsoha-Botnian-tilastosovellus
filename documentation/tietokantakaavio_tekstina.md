## Tietokantakaavio tekstimuodossa

[Player|(pk)id:Integer;name:String;number:Integer], [Goal|(pk)id:Integer;(fk)game_id:Integer;scorer_id:Integer;assist_id:Integer], [Penalty|(pk)id:Integer;(fk)game_id:Integer;player_id:Integer;minutes:Integer], [Game|(pk)id:Integer;date:Date;opponent:String;botnia_goals:Integer;opponent_goals:Integer]
[GamePlayer|(fk)game_id:Integer;(fk)player_id:Integer]
[Player]1..2-*[Goal]
[Goal]*-1[Game]
[Penalty]*-1[Game]
[Player]1-*[Penalty]
[Player]1-*[GamePlayer]
[GamePlayer]*-1[Game]
