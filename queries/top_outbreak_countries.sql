select country, count(*) as DISEASE_COUNT
from outbreaks
group by country
order by count(*) desc limit 10
