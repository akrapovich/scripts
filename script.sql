select
    date_format(created_at, '%Y-%m-%d') day,
    SEC_TO_TIME(sum(if(power_on=1,1,0))*60) power_on,
    SEC_TO_TIME(sum(if(power_on = 0, 1, 0))*60) power_off,
    SEC_TO_TIME(count(*)*60) total,
    SEC_TO_TIME(sum(if(external_ip,1,0))*60) online,
    group_concat(distinct INET_NTOA(external_ip)) ips
from power_tracker
group by year(created_at), month(created_at), day(created_at)
