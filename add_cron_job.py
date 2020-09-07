#!/usr/bin/python3
"""
  Add cron job that runs every 30 days
    usage:
       ./add_cron_job.py <script> <directory>
    example:
       ./add_cron_job.py compress_files.py /var/log/
"""
import sys
from crontab import CronTab

def add_cron_job(script_path:str,dir_to_compress:str):
    """
    Add cron job that runs every 30 days
    :param script_path:
    :param dir_to_compress:
    :return: True
    """
    cron = CronTab()
    command="00 00 * * *  test $(( $(date +\%s)/24/60/60\%30 )) = 26 && {} {}".format(script_path,dir_to_compress)
    job = cron.new(command=command)
    cron.write()
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    add_cron_job(sys.argv[1],sys.argv[2])