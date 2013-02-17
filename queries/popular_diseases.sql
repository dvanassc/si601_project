select disease, count(*) as DISEASE_COUNT
from health_data_csv
group by disease
order by count(*) desc