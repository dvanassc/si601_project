select disease, count(*) as OUTBREAK_COUNT
from outbreaks
group by disease
order by count(*) desc