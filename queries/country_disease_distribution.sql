-- Pull population data from http://en.wikipedia.org/wiki/List_of_countries_by_population to get a per capita?
select country, count(disease) as OUTBREAK_COUNT
from outbreaks
group by country