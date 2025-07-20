

# python script to read a plain text log file

with open('app.log', 'r') as file: 
    logs = file.readlines()


# If your logs are in JSON format, you can use the json library to parse them
import json
with open('logs.json', 'r') as file:
    logs = json.load(file)




# 5. Common Log Analysis Tasks with Python
# 1 Filtering logs
import re
# This filters out only the lines that contain “ERROR,” allowing you to quickly focus on problematic areas.
error_logs = [log for log in logs if re.search('ERROR', log)]


# 2 Aggregating logs
import pandas as pd 
