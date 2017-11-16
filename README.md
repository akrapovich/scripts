# show db data
select INET_NTOA(external_ip), created_at from power_tracker;

# add to crontab
* * * * * sh /home/serg/scripts/get_external_ip.sh >> /var/log/external_ip.log
