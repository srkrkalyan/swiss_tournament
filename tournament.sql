-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create table player (
p_id SERIAL primary key,
p_name TEXT
);

create table match (
m_id SERIAL primary key,
winner integer references player(p_id),
loser integer references player(p_id)
);


create view player_wins as
	select p.p_id, count(match.winner) as wins from player p left join match on p.p_id = match.winner group by p.p_id;


create view player_loss as
	select p.p_id, count(match.loser) as loss from player p left join match on p.p_id = match.loser group by p.p_id;


create view player_standings as
	select pw.p_id, pw.wins, pl.loss, pw.wins+pl.loss as matches 
	from player_wins pw join player_loss pl on pw.p_id = pl.p_id 
	group by pw.p_id, pw.wins, pl.loss order by pw.wins desc;


create view pairing_ids as 
	select ps1.p_id as player1, ps2.p_id as player2 from 
	player_standings ps1 join player_standings ps2 on ps1.wins = ps2.wins where ps1.p_id < ps2.p_id;


create view pairings as
	select pa.player1 as id1, p1.p_name as name1, pa.player2 as id2, p2.p_name as name2 
            from pairing_ids pa, player p1, player p2 where 
            pa.player1 = p1.p_id and pa.player2 = p2.p_id
            ;