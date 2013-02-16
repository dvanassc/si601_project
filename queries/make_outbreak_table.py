import sqlite3 as sqlite
import sys
'''COUNTING RULES - OUR DEFINITION : Same country, same date, same disease --> 1 outbreak
  Initial Draft -- Allison Bailey
'''

#Get the data from the main database
with sqlite.connect('health.db') as con: 
  cur = con.cursor() 
  cur.execute("SELECT country, disease, report_date FROM health_data_csv")
  rows = cur.fetchall()
  
  data=[]
  for row in rows:
    x = row[2].split()
    l=(row[0],row[1],row[2],x[0])
    data.append(l)

#Create new table where we'll add the short date (just the date - not timestamp) and run query on data  
  cur.execute("DROP TABLE IF EXISTS country_disease_reports")
  cur.execute("CREATE TABLE country_disease_reports(country TEXT, disease TEXT, report_date TEXT, date_short TEXT)")
  cur.executemany("INSERT INTO country_disease_reports VALUES(?, ?, ?, ?)", data)


#Join table with itself to compare rows on three column values
with sqlite.connect('health.db') as con: 
  cur = con.cursor() 
  cur.execute('''
    select DISTINCT a.country, a.disease, a.date_short
    From country_disease_reports a, country_disease_reports b
    where a.country = b.country
      AND a.disease = b.disease
	    AND a.date_short = b.date_short;''')
  rows = cur.fetchall()
  #print rows

#Dump results into "outbreaks" table that we can subsequently use for outbreak-based analysis  
  cur.execute("DROP TABLE IF EXISTS outbreaks")
  cur.execute("CREATE TABLE outbreaks(country TEXT, disease TEXT, date_short TEXT)")
  cur.executemany("INSERT INTO outbreaks VALUES (?, ?, ?)", rows)


