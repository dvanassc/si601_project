SELECT disease, count(*) AS outbreak_count, count(distinct country) AS num_countries, sum(report_instances) AS total_reports,
  cast(sum(report_instances)/count(*) as FLOAT) AS reports_per_outbreak
FROM outbreaks
GROUP BY disease
ORDER BY count(*) DESC