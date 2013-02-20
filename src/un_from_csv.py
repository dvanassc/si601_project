#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, csv
import sqlite3 as sqlite
'''python2 un_from_csv.py

Draft by Allison Bailey (ambail)

Purpose: Create Population Table Based on UN CSV for 2012 Population Estimates
(Made in 2010). Apparently, the UN only comes out with new estimates every
two years - we're in between updates.

References: http://stackoverflow.com/questions/2969044/python-string-escape-vs-unicode-escape
'''
def make_unicode(x):
    try:
        return unicode(x)
    except UnicodeDecodeError:
        byte_text = str(x).encode('string_escape')
        return unicode(byte_text)


with open('../HealthDataMap/un_pop_data.csv','rU') as csvfile:
    popreader = csv.reader(csvfile)
    data = []
    for row in popreader:
        x = row[65].split(',')
        pop = ''.join(x)
        l =(make_unicode(row[0]),make_unicode(row[1]),float(pop))
        data.append(l)        
        
with sqlite.connect('../HealthDataMap/health.db') as con: 
  cur = con.cursor() 
  cur.execute("DROP TABLE IF EXISTS populations")
  cur.execute("CREATE TABLE populations(Country TEXT, ISO_Code TEXT, Population_2012 FLOAT)")
  cur.executemany("INSERT INTO populations VALUES (?, ?, ?)", data)

