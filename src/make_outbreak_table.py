import sqlite3 as sqlite
import sys
'''COUNTING RULES - OUR DEFINITION : Same country, same date, same disease --> 1 outbreak
python2 make_outbreak_table.py
'''

#Get the data from the main database
with sqlite.connect('../HealthDataMap/health.db') as con: 
  cur = con.cursor() 
  cur.execute('''select country, disease, date(report_date) as short_date, count(*), avg(rating)
                from health_data_csv
                group by country, disease, date(report_date)''')
  rows = cur.fetchall()
  
#Dump results into "outbreaks" table that we can subsequently use for outbreak-based analysis  
  cur.execute("DROP TABLE IF EXISTS outbreaks")
  cur.execute("CREATE TABLE outbreaks(country TEXT, disease TEXT, date_short TEXT, report_instances INT, avg_rating FLOAT)")
  cur.executemany("INSERT INTO outbreaks VALUES (?, ?, ?, ?)", rows)


