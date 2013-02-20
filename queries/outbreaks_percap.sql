/*ALLISON -- Currently this query yields unexpected results for the percap
calculation -- I'll continue to investigate, but let me know if you see any
obvious errors.*/

select o.country, count(o.disease) as incidents,p.population_2012,(count(o.disease)/p.population_2012) as incident_percap
from outbreaks as o
join populations as p on (o.country=p.country)
group by o.country
order by incident_percap desc