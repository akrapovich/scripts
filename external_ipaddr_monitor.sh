#!/bin/bash
GET_IP_ADDR="$(dig +short myip.opendns.com @resolver1.opendns.com)"
EMAIL_TITLE="Server IP"
CUR_IP_ADDR=".cur_ipaddr"




if [ -f $CUR_IP_ADDR ] && [ `cat $CUR_IP_ADDR` = `echo $GET_IP_ADDR` ]; then
    echo "same ip addres, nothing to do"
else
    echo "send new ip addr!"
    echo $GET_IP_ADDR > $CUR_IP_ADDR
    mail -s $EMAIL_TITLE sergey.g@ezscratch.com < $CUR_IP_ADDR
fi


