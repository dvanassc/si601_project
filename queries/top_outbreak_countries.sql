select country, count(*) as OUTBREAK_COUNT
from outbreaks
group by country
order by count(*) desc limit 10
