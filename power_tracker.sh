#!/bin/bash                                                                                                                                                                                                 

ROUTER_IP='192.168.5.1'
DATETIME_FORMAT="%Y-%m-%dT%H:%M:%S"
DATETIME=$(date +$DATETIME_FORMAT)
IP_ADDR="$(dig +short myip.opendns.com @resolver1.opendns.com)"


# if [ ping -c 1 "$ROUTER_IP" >/dev/null ]; then

if ! ping -c 1 "$ROUTER_IP" >/dev/null ; then
    POWER_ON=0
else
    POWER_ON=1
fi


SQL="insert into power_tracker values (INET_ATON('$IP_ADDR'),$POWER_ON,'$DATETIME')"
echo "$SQL"
mysql -u root power_tracker -e "$SQL"
