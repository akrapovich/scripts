#!/bin/bash
DEVID=`xinput | grep TouchPad | cut -f2 -d'=' | awk '{print $1}'`
xinput set-prop $DEVID "Device Enabled" 0
