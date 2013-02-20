select o.country, count(*) as incidents,p.population_2012,(count(*)/p.population_2012) as incident_percap
from outbreaks as o
join populations as p on (o.country=p.country)
group by o.country
order by incident_percap desc