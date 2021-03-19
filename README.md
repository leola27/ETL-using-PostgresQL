Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

The analytics team at Sprakify is interested in understanding what songs users are listening to. 
The project provides such data in form of relational database, which means that it is easy for users to 
perform various, even complicated queries which are not defined in advance.

State and justify your database schema design and ETL pipeline.  

The database schema design is snowflake. it is benefitial considering the goals of analytics team since it 
organises the data in the fact table, showing how and when users play songs, and several dimension tables, 
providing details on a particular dimension of the data (song,user, artist,time).

[Optional] Provide example queries and results for song play analysis.

To understand in which location most users are: 
"with temp as (Select  location, count(*) AS cnt from songplays group by location) select location,cnt from temp order by cnt desc"

To understand if users pay or not: 
"Select level, count(*)  from songplays group by level"

To understand at what time users listen to the songs mostly: 
"Select hour, count(*)  from time  group by hour"
