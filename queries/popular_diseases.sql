select disease, count(*) as DISEASE_COUNT
from outbreaks
group by disease
order by count(*) desc