select country, disease, count(*) as DISEASE_COUNT
from health_data_csv
group by country, disease
order by country, count(*) desc