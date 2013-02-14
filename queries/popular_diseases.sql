select disease, count(*)
from health_data_csv
group by disease
order by count(*) desc