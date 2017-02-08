#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("delete from match;")
    db.commit()
    db.close()
    return


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("delete from player;")
    db.commit()
    db.close()
    return

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("select count(*) as count from player;")
    count = cursor.fetchall()[0][0]
    db.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("insert into player(p_name) values (%s)",(name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cursor = db.cursor()
    query = """select ps.p_id, p.p_name, ps.wins, ps.matches from 
            player_standings ps, player p where ps.p_id = p.p_id order by ps.wins desc;"""
    cursor.execute(query)
    list_player_standings = cursor.fetchall()
    db.close()
    return list_player_standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("insert into match (winner,loser) values(%s,%s);",(winner,loser,))
    db.commit()
    db.close()
 


def trim_swiss_pairs(pairings):
    """Generates and returns swiss_pairs from given possible pairings 

    Args:
        pairings: All possible pairings for a game round
    """

    swiss_pairs = pairings
    for i in range(0,len(swiss_pairs)):
        if i < len(swiss_pairs):
            id1 = swiss_pairs[i][0]
            id2 = swiss_pairs[i][2]
            for each in swiss_pairs[i+1:]:
                if id1 == each[0] or id1 == each[2]:
                    swiss_pairs.remove(each)
                elif id2 == each[0] or id2 == each[2]:
                    swiss_pairs.remove(each)
    return swiss_pairs


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    query = "select * from pairings;"
    db = connect()
    cursor = db.cursor()
    cursor.execute(query)
    pairings = cursor.fetchall()
    db.close()
    return trim_swiss_pairs(pairings)

