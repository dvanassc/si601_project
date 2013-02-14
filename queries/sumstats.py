import sqlite3 as sqlite

# Average rating per country and count per country
with sqlite.connect('HealthDataMap/health.db') as con:
  cur=con.cursor()
  cur.execute("SELECT country, avg(rating), count(*) FROM health_data_csv GROUP BY country")
  rows=cur.fetchall()
  for row in rows:
    print row
    
# Better understanding the geographical text units : Place/Country summary stats
with sqlite.connect('HealthDataMap/health.db') as con:
  cur=con.cursor()
  cur.execute("SELECT DISTINCT country, place, count(*) FROM health_data_csv GROUP BY country, place")
  rows=cur.fetchall()
  f=open('sumstats.txt','w')
  for row in rows:
    t=(row[0],row[1],str(row[2])) # Create new tuple to replace int with str
    line='\t'.join(t)
    f.write(line.encode('utf8')+'\n')
# TBD more code on pulling apart the text in the "place" field. Compare with lat/long, too?
