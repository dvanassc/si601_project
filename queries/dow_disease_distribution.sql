select case
        when strftime('%w', report_date) = '0' then 'Sunday'
        when strftime('%w', report_date) = '1' then 'Monday'
        when strftime('%w', report_date) = '2' then 'Tuesday'
        when strftime('%w', report_date) = '3' then 'Wednesday'
        when strftime('%w', report_date) = '4' then 'Thursday'
        when strftime('%w', report_date) = '5' then 'Friday'
        when strftime('%w', report_date) = '6' then 'Saturday'
        else strftime('%w', report_date)
        end as DOW, disease, count(*) as DISEASE_COUNT
from health_data_csv
where date(report_date) between date('2012-08-05') and ('2012-10-27')
group by strftime('%w', report_date), disease
