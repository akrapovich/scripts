# show db data
select INET_NTOA(external_ip), power_on, created_at from power_tracker;

# show day result
select count(*) total, sum(if(power_on=1,1,0)) online, sum(if(power_on = 0, 1, 0)) ofline, date_format(created_at, '%Y-%m-%d') day from power_tracker group by year(created_at), month(created_at), day(created_at);

# add to crontab
* * * * * sh /home/serg/scripts/get_external_ip.sh >> /var/log/external_ip.log
