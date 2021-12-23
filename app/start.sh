#!/bin/bash

# Start the run once job.
echo "Docker container has been started"
ntpd -gq > /dev/null 2> /dev/null
service ntp start > /dev/null 2> /dev/null
echo "Current date and time:"
date
if [[ -z $CRON_SCHEDULE ]]; then
    echo "There is no schedule"
else
    echo "Cron schedule: ${CRON_SCHEDULE//X/*}"
fi

declare -p | grep -Ev 'BASHOPTS|BASH_VERSINFO|EUID|PPID|SHELLOPTS|UID' > /container.env

if [[ -z $CRON_SCHEDULE ]]; then
    exec python3 /app/currency.py
else
    echo "SHELL=/bin/bash
    BASH_ENV=/container.env
    ${CRON_SCHEDULE//X/*} /app/currency.py
    # This extra line makes it a valid cron" > scheduler.txt
    crontab scheduler.txt
    exec cron -f
fi