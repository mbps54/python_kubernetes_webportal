#!/bin/bash

# Start the run once job.
echo "Docker container has been started"
ntpd -gq > /dev/null 2> /dev/null
service ntp start > /dev/null 2> /dev/null
echo "Current date and time:"
date
if [[ -z $CRON_SCHEDULE ]]; then
    echo "The script will executes only once"
else
    echo "he script will be scheduled: ${CRON_SCHEDULE//X/*}"
fi

declare -p | grep -Ev 'BASHOPTS|BASH_VERSINFO|EUID|PPID|SHELLOPTS|UID' > /container.env

python3 /app/app-exchange_cbrf.py

if [[ -z $CRON_SCHEDULE ]]; then
    echo "."
else
    echo "SHELL=/bin/bash
    BASH_ENV=/container.env
    ${CRON_SCHEDULE//X/*} /app/app-exchange_cbrf.py
    # This extra line makes it a valid cron" > scheduler.txt
    crontab scheduler.txt
    exec cron -f
fi