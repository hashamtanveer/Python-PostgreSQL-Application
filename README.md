# Python-PostgreSQL-Application
A simple implementation of how we can connect a Python application to PostgreSQL.

1.	Create a database in PostgreSQL named footballdb. 
2.	The database will be populated with the Kaggle data found in https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017
3.	The dataset includes international football results from 1872 to 2021. It contains two CSV files with contents as follows:

results.csv includes the following columns:

date - date of the match
home_team - the name of the home team
away_team - the name of the away team
home_score - full-time home team score including extra time, not including penalty-shootouts
away_score - full-time away team score including extra time, not including penalty-shootouts
tournament - the name of the tournament
city - the name of the city/town/administrative unit where the match was played
country - the name of the country where the match was played
neutral - TRUE/FALSE column indicating whether the match was played at a neutral venue
shootouts.csv includes the following columns:
date - date of the match
home_team - the name of the home team
away_team - the name of the away team
winner - winner of the penalty-shootout

4.	Download the dataset with the two CSV files from the Kaggle website
5.	Create a file a3_create_tables.sql with the SQL statements to create and load the needed tables. Make sure that your script is repeatable (meaning that you can run it right after you just ran it – Hint: include drop table if exists).
![image](https://user-images.githubusercontent.com/60246728/146070418-e47d790f-c2d6-4fcc-8049-808004d61a14.png)
