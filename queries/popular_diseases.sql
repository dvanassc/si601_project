select disease, count(*) as OUTBREAK_COUNT, sum(report_instances) as TOTAL_REPORTS
from outbreaks
group by disease
order by count(*) desc