import sys, csv
import sqlite3 as sqlite
'''python2 un_from_csv.py

Draft by Allison Bailey (ambail)

Purpose: Create Population Table Based on UN CSV for 2012 Population Estimates
(Made in 2010), obtained from Guardian UK: 
http://www.guardian.co.uk/news/datablog/2011/may/06/world-population-country-un#data

Apparently, the UN only comes out with new estimates every
two years - we're in between updates.
'''

with open('../HealthDataMap/un_pop_data.csv','rU') as csvfile:
    popreader = csv.reader(csvfile)
    data = []
    for row in popreader:
        l =(row[0],row[1],row[65])
        data.append(l)        
        
with sqlite.connect('../HealthDataMap/health.db') as con: 
  con.text_factory = str
  cur = con.cursor() 
  cur.execute("DROP TABLE IF EXISTS populations")
  cur.execute("CREATE TABLE populations(Country TEXT, ISO_Code TEXT, Population_2012 INTEGER)")
  cur.executemany("INSERT INTO populations VALUES (?, ?, ?)", data)

