#!/bin/bash
mysql -u root power_tracker -t -e  "select count(*) total, sum(if(power_on=1,1,0)) online, sum(if(power_on = 0, 1, 0)) ofline, date_format(created_at, '%Y-%m-%d') day from power_tracker group by year(created_at), month(created_at), day(created_at)"
