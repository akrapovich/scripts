#!/bin/bash
mysql -u root power_tracker -t -e "
select
date_format(created_at, '%Y-%m-%d') day,
SEC_TO_TIME(sum(if(power_on=1,1,0))*60) online,
SEC_TO_TIME(sum(if(power_on = 0, 1, 0))*60) ofline,
SEC_TO_TIME(count(*)*60) total
from power_tracker
group by year(created_at), month(created_at), day(created_at)"
