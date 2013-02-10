'''
Created on Feb 9, 2013

@author: Derek
'''
import sqlite3
import json
import csv

CONN = sqlite3.connect("../HealthDataMap/health.db")
CONN.text_factory = str
CURSOR = CONN.cursor()
COMMIT_POINT = 5000

def create_database():
  CURSOR.execute('DROP TABLE IF EXISTS health_data_csv')
  CURSOR.execute("""CREATE TABLE health_data_csv
                    (country text, place text, latitude real, longitude real, disease text, report_date text, 
                     summary text, description text, rating integer, feed text, link text) 
                 """)
  CURSOR.execute('DROP TABLE IF EXISTS health_data_json')
  CURSOR.execute("""CREATE TABLE health_data_json
                    (country text, place text, latitude real, longitude real, disease text, report_date text, 
                     summary text, description text, rating integer, feed text, link text) 
                 """)

def insert(data, ext):
  if data and len(data) > 0:
    CURSOR.executemany("INSERT INTO health_data" + ext + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    CONN.commit()

def load_data(filename, load_format):
  if load_format == 'json':
    load_json(filename)
  elif load_format == 'csv':
    load_csv(filename)
  else:
    print 'ERROR: Invalid format, please specify 1 of "json" or "csv".'

def load_json(filename):
  json_file = open(filename, 'rU')
  i = 0
  data = []
  for line in json_file:
    entries = json.loads(line)
    for entry in entries:
      for alert in entry['alerts']:
        data.append((entry['country'], entry['place_name'], float(entry['lat']), float(entry['lng']), alert['disease'], alert['date'], alert['summary'], alert['descr'], int(float(alert['rating']['rating'])), alert['feed'], alert['link']))
        i += 1
        if i % COMMIT_POINT == 0:
          insert(data, '_json')
          data = []
  json_file.close()
  insert(data, '_json')

def load_csv(filename):
  with open(filename, 'rU') as f:
    reader = csv.reader(f, delimiter=',')
    i = 0
    data = []
    is_first = True
    for row in reader:
      if is_first:
        is_first = False
        continue
      data.append((row[0], row[1], float(row[2]), float(row[3]), row[4], row[5], row[6], row[7], int(float(row[8])), row[9], row[10]))
      i += 1
      if i % COMMIT_POINT == 0:
        insert(data, '_csv')
        data = []
    insert(data, '_csv')

def main():
  create_database()
  load_data('../HealthDataMap/healthMapFeed.json', 'json')
  load_data('../HealthDataMap/completeTable.csv', 'csv')

if __name__ == '__main__':
  main()
