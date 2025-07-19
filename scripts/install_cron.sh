#!/bin/bash

# Get absolute path to the project root (assuming this script is in scripts/)
PROJECT_ROOT="$(cd "$(dirname "$0")"/.. && pwd)"

CRON_JOB="*/5 * * * * cd $PROJECT_ROOT && ./scripts/run_bot.sh >> $PROJECT_ROOT/run_bot.log 2>&1"

# Install the cronjob (appends if already present)
(crontab -l 2>/dev/null | grep -Fv "$PROJECT_ROOT/scripts/run_bot.sh"; echo "$CRON_JOB") | crontab -

echo "Cronjob installed:"
echo "$CRON_JOB"