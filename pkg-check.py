# File: pkg-check.py
# Author: David Marin
# Created: 9/28/2025
# Description: This is a Python script that writes a cron job to output packages that need updates. This script checks
#              for packages that need to be updated, outputs the list to a file, and runs as a cron task each week.
#
# IMPORTANT NOTE: This script should be run inside of a WSL terminal.

import subprocess

subprocess.run(['sudo', 'apt', 'update'])
update_list = subprocess.run(['apt', 'list', '--upgradable'], capture_output=True, text=True)
update_list = update_list.stdout.strip().split('\n')

with open("/var/tmp/update-list.txt", "w") as f:
    f.write("You gotta update these packages... they're outdated.\n\n")
    for i in range(len(update_list)):    
        f.write(update_list[i])
        f.write('\n')

cronjob = '0 8 * * 1 /mnt/c/Users/david/cs310/cs310-package-update-checker/pkg-check.py'
subprocess.run(['bash', '-c', f'(crontab -l 2>/dev/null; echo "{cronjob}") | crontab -'], check=True)