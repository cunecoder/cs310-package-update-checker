# CS310: Week 5 - Package Update Checker

## Summary

The goal of this assignment is to write a cron job script that outputs the packages that need updates.
The script should:
- Check for packages that need to be updated
- Output that list to a file
- Be run as a cron task each week

Your submission will include:
- A link to your version of this GitHub Repo
- A `.txt`, `.md`, `.org` written report
- A script named `pkg-check.<ext>` (either .py or .sh)

You may write this in Python or Bash

## Assignment

In this lab, you will:
- Create a script that checks `apt` if there are any updates for the package.
    - This necessarily means running `apt update` before
- Grab the list of outputted packages
- Write that list to a file that you can check, like `/var/tmp/update-list.txt`
- Install this as a cron job that runs weekly

## Report

Your report is to have the following title: **CS 310 - W5 Package Update Checker.<ext>**

Your report is to answer the following questions in 1-2 sentences:
1. How did you get the list of packages?
2. What is the crontab sequence to run the script?
3. Since this script would require root, how do you install a crontab for root?

## Resources
- [APT Man Page](https://manpages.debian.org/buster/apt/apt.8.en.html)
- [Redirecting Output in Bash](https://www.geeksforgeeks.org/linux-unix/input-output-redirection-in-linux/)
- [Crontab Man Page](https://www.man7.org/linux/man-pages/man5/crontab.5.html)
