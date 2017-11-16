#!/bin/bash
DATETIME_FORMAT="%Y-%m-%dT%H:%M:%S"
CUR_DATETIME=$(date +$DATETIME_FORMAT)
MYIP="$(dig +short myip.opendns.com @resolver1.opendns.com)"

echo "$MYIP $CUR_DATETIME"
