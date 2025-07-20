# 1. Linux Logging and journalctl

# Many applications log their messages using a service called systemd-journald

# These logs are not stored in plain text files by default; instead, 
# they are stored in a binary format in directories like /var/log/journal/

# To view these logs, Linux provides a powerful command-line tool called journalctl. 
# You can use journalctl to read and search logs easily:

# journalctl                     # Show all logs
# journalctl -u nginx            # Show logs for the nginx service
# journalctl -b                  # Show logs from the current boot
# journalctl --since "2 hours ago"  # Show logs from the last 2 hours
# journalctl -u ssh --since yesterday # SSH logs from yesterday
# journalctl -xe                 # Show recent logs with priority and error details

# It’s commonly used in production environments to check logs without needing to open individual log files. 

# While some traditional apps still write logs directly to files like /var/log/syslog, /var/log/nginx/access.log, or /var/log/auth.log, 
# more modern applications integrate with systemd so their logs can be managed consistently with journalctl.



#  2. Saving Logs in a File

# The simplest method of logging is to write logs to a file on the local disk. 
# This is especially useful when you’re running a small application on one machine.

import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.info("Application started")
logging.warning("This is a warning!")
logging.error("oops! an error has happened")

# This writes logs to a file named app.log


#  3  What Is Log Rotation?

# If you keep writing to the same file forever, the file can become huge and take up disk space. 
# Log rotation is the process of automatically moving old logs into separate files and starting a new one

from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# If you don’t rotate logs, they could:

# Fill up your disk
# Slow down your application
# Be hard to search and manage


# Sending Logs to Centralized Servers Using Log Agents

# we use log agents to collect logs and send them to centralized log management systems like 
# Elasticsearch, Splunk, or Datadog

# What Are Log Agents?
# A log agent is a background program that:

# Watches your log files
# Reads new log entries
# Converts them to a standard format (like JSON)
# Sends them in batches to a central log server


# Popular Log Agents:
# Fluentd
# Filebeat
# Logstash
# Datadog Agent

# 4 Visualizing Logs Using Dashboards
# Reading raw log files is not efficient, especially when you have thousands of log entries. 
# Visualization tools make it easier by showing charts, graphs, and dashboards.

# Popular Visualization Tools:

# Kibana (used with Elasticsearch)
# Grafana Loki
# Splunk
# New Relic
# Apica

# These tools allow you to:

# Search logs by keyword or time range
# Create alerts for certain error patterns
# Build dashboards to track system health

