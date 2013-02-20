select country, disease, count(*) as DISEASE_COUNT
from outbreaks
group by country, disease
order by country, count(*) desc