'''
Created on Feb 16, 2013

@author: Derek
'''

import os
import re
import csv
import sqlite3 as sqlite
import sys

CONN = sqlite.connect("../HealthDataMap/health.db")
CONN.text_factory = str

def read_file(filename):
  input_file = open(filename, 'rU')
  sql = ''
  for line in input_file:
    sql += line
  return sql

def execute_query(sql, output_file_name):
  output_file = open('../output/' + output_file_name, 'wb')
  writer = csv.writer(output_file, delimiter='\t')
  cur = CONN.cursor()
  
  headers = []
  res = cur.execute(sql)
  for md in res.description:
    headers.append(md[0])
  writer.writerow(headers)
  
  rows = cur.fetchall()
  for row in rows:
    writer.writerow(row)

def main():
  try:
    for dirname, dirnames, filenames in os.walk('../queries'):
      for filename in filenames:
        sql = read_file(os.path.join(dirname, filename))
        execute_query(sql, re.sub(r'[.]sql', '.tsv', filename))
  except sqlite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
  finally:
    if CONN:
      CONN.commit()
      CONN.close()

if __name__ == '__main__':
  main()
