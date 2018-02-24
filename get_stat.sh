#!/bin/bash
mysql -u root power_tracker -t -e "$(< script.sql)"
