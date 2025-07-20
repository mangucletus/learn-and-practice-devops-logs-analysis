

# python script to read a plain text log file

with open('app.log', 'r') as file: 
    logs = file.readlines()


# If your logs are in JSON format, you can use the json library to parse them
import json
with open('logs.json', 'r') as file:
    logs = json.load(file)




#   Common Log Analysis Tasks with Python

# 1 Filtering logs

import re
# This filters out only the lines that contain “ERROR,” allowing you to quickly focus on problematic areas.
error_logs = [log for log in logs if re.search('ERROR', log)]


# 2 Aggregating logs

import pandas as pd 
# This code snippet will give you a count of how many times each type of error has occurred.
log_df = pd.DataFrame(logs, columns=['timestamp', 'log_level', 'message'])
error_counts = log_df[log_df['log_level']=='ERROR'].groupby('message').size()


# 3 Time-Based Log Analysis

from datetime import datetime
# This allows you to calculate the time between events or detect time-based anomalies in the log data.
for log in logs:
    timestamp = datetime.strptime(log['timestamp'], '%Y-%m-%d #H:%M:#S')
    # Further analysis based on the timestamp



#   Advanced Log Analysis with Python

# 1 Pattern Detection

# example, you can write a script to identify multiple failed login attempts in a short period, 
# which might indicate a brute-force attack

failed_logins = [log for log in logs if 'failed login' in log['message']]


# 2 Automating Log Analysis Workflows

# ou can set up Python scripts to run on a schedule and automatically analyze logs, 
# sending alerts if something abnormal is detected.

# For example, you can use a cron job (on Linux) to schedule a Python script to check logs every hour:

# 0 * * * * /usr/bin/python3 /path/to/log_analysis_script.property

# This automates the log monitoring process, notifying your team of any critical issues 
# without the need for constant manual checks.


# 3 Python Log Analysis in CI/CD Pipelines

# For example, after deploying an application, a Python script can analyze 
# the logs to check for any errors or performance issues. If a problem 
# is detected, the script can trigger an alert or rollback the deployment:
if 'ERROR' in logs:
    rollback_deployment()