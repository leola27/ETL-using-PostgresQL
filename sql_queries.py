# DROP TABLES

songplay_table_drop = "Drop table IF EXISTS songplays"
user_table_drop = "Drop table IF EXISTS users"
song_table_drop = "Drop table IF EXISTS songs"
artist_table_drop = "Drop table IF EXISTS artists"
time_table_drop = "Drop table IF EXISTS time"

# CREATE TABLES



songplay_table_create = "CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY NOT NULL, start_time timestamp NOT NULL, user_id varchar(4) NOT NULL, level varchar(10), song_id varchar(50), artist_id varchar(50), session_id varchar(50), location varchar(50), user_agent varchar(200))"

#user_id, first_name, last_name, gender, level
user_table_create = "CREATE TABLE IF NOT EXISTS users (user_id varchar(4) PRIMARY KEY NOT NULL, first_name varchar(50), last_name varchar(50), gender varchar(1), level varchar(10));"

#song_id, title, artist_id, year, duration
song_table_create = "CREATE TABLE IF NOT EXISTS songs (song_id varchar(50) PRIMARY KEY NOT NULL, title varchar(100), artist_id varchar(50) NOT NULL, year int, duration numeric)"

#artist_id, name, location, latitude, longitude
artist_table_create = "CREATE TABLE IF NOT EXISTS artists (artist_id varchar(50) PRIMARY KEY NOT NULL, name  varchar(100), location varchar(100), latitude varchar(100), longitude varchar(100))"

#start_time, hour, day, week, month, year, weekday
time_table_create = "CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY NOT NULL, hour numeric, day numeric, week numeric, month numeric, year numeric, weekday numeric) ON CONFLICT DO NOTHING"

# INSERT RECORDS

songplay_table_insert ="Insert INTO songplays  ( start_time, user_id , level,song_id,artist_id, session_id, location, user_agent) values (%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING"


user_table_insert = "Insert INTO users (user_id , first_name, last_name, gender,level) values (%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level"

song_table_insert = "Insert INTO songs (song_id, title, artist_id, year,duration) values (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING"


artist_table_insert = "Insert INTO artists (artist_id, name, location, latitude,longitude) values (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING"


time_table_insert = "Insert INTO time (start_time , hour, day, week,month, year, weekday) values (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING"

# FIND SONGS

song_select = "SELECT s.song_id, a.artist_id FROM songs s INNER JOIN artists a ON s.artist_id = a.artist_id WHERE s.title = %s AND a.name = %s AND s.duration = %s And s.song_id is not null  and a.Artist_id is not null"

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]