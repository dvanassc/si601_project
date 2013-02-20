-- Average and max number reports 
SELECT country, sum(Report_Instances), count(*), avg(Report_Instances),  max(Report_Instances) FROM outbreaks GROUP BY country