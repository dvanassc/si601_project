select strftime('%w', report_date), count(*)
from health_data_csv
where date(report_date) between date('2012-08-05') and ('2012-10-27')
group by strftime('%w', report_date)