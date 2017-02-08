What is this?

A Python solution that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This solution was developed using TDD (Test Driven Development)


Contents?

The file tournament.sql contains database schema in form of SQL commands.

The file tournament.py contains the actual Python solution to keep track of players and matches in a game tournament.

The file tournament_test.py contains the unit tests for all the functions implemented in tournament.py


Run Locally?

The solution uses PostgreSQL as backend database. So, this needs to be setup in local machine. (Reference: https://www.postgresql.org/download/)

The python solution uses psycopg2 module. So, this needs to be setup in local machine. (Reference: http://initd.org/psycopg/docs/install.html)


Installation?

Clone the repository to local after setting up PostgreSQL DB and Psycopg2 Python API. Please use Python 2.7 for running this solution.



