select h.country, count(*) as reports,p.population_2012,(count(*)/p.population_2012) as reports_country_percap
from health_data_csv as h
join populations as p on (h.country=p.country)
group by h.country
order by reports_country_percap desc