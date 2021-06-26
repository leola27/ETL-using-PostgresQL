# Udacity Data Engineer Nanodegree project

## Data Modeling with Postgres

### Introduction

The analytics team at Sprakify is interested in understanding what songs users are listening to.The project provides such data in form of relational database, which means that it is easy for users to perform various, even complicated queries which are not defined in advance.

### Database schema design and ETL process

The database schema design is snowflake. It is benefitial considering the goals of analytics team since it organises the data in the fact table, showing how and when users play songs, and several dimension tables, providing details on a particular dimension of the data (song,user, artist,time).
#### Fact Table
songplays - records in log data associated with song plays i.e. records with page NextSong:songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
#### Dimension Tables
##### users
users in the app: user_id, first_name, last_name, gender, level
##### songs
songs in music database: song_id, title, artist_id, year, duration
##### artists
artists in music database: artist_id, name, location, latitude, longitude
##### time 
timestamps of records in songplays broken down into specific units: start_time, hour, day, week, month, year, weekday

### Files in repository
Data directory contains JSON files which are processed by ETL
#### test.ipynb 
displays the first few rows of each table to let you check your database.
#### create_tables.py 
drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
#### etl.ipynb 
reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
#### etl.py 
reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
#### sql_queries.py 
contains all your sql queries, and is imported into the last three files above.
