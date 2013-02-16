select country, count(*)
from outbreaks
group by country
order by count(*) desc limit 10
