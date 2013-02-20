-- Average and max number reports per disease outbreak per country
SELECT country, sum(Report_Instances) as TOTAL_REPORTS, count(*) as TOTAL_OUTBREAKS, 
  avg(Report_Instances) as AVG_REPORTS_PER_OUTBREAK,  max(Report_Instances) as MAX_REPORT_INSTANCES 
FROM outbreaks 
GROUP BY country