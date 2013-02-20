select country, disease, count(*) as OUTBREAK_COUNT
from outbreaks
group by country, disease
order by country, count(*) desc