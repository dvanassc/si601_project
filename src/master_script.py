'''
Created on Feb 16, 2013

@author: Derek
'''

## 1 - Create health.db and load the csv/json files into it
execfile('load_hd_map.py')

## 2 - Create an outbreak table that compresses diseases by date
execfile('make_outbreak_table.py')

## 3 - Create table of population data from UN estimates by country for 2012
execfile('un_from_csv.py')

## 4 - Run all sql queries found in the ../queries folder
execfile('run_simple_queries.py')
