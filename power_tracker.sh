#!/bin/bash                                                                                                                                                                                                 
# TODO: ping router
DATETIME_FORMAT="%Y-%m-%dT%H:%M:%S"
DATETIME=$(date +$DATETIME_FORMAT)
IP_ADDR="$(dig +short myip.opendns.com @resolver1.opendns.com)"
SQL="insert into power_tracker values (INET_ATON('$IP_ADDR'),'$DATETIME')"

mysql -u root power_tracker -e "$SQL"
echo "$SQL"
