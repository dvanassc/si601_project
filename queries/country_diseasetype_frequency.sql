select country, disease, count(*)
from health_data_csv
group by country, disease
order by country, count(*) desc