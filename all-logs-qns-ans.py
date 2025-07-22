# QUESTION 1

# you are working with web server log files located in the /var/logs/ directory. 
# each log file ( eg. events.log, traffic.log, etc.) contains details about http requests made to the server, including the date, time, request type, file requested, protocol version. status code, and the size of the returned object in bytes.

# Each log line in any of these log files is formatted as follows:

# [15/Sep/2023:13:25:34 -0400] "POST /upload/file HTTP/1.1" 201 48299
# WHERE:

# . The first part ([15/Sep/2023:13:25:34 -0400]) is the timestamp.
# . "POST /upload/file HTTP/1.1" is the request line, including the HTTP method, file requested, and protocol version.
# . 201 is the HTTP status code.
# . 48290 is the size of the returned object in bytes.

# Task
# Calculate the total number of successful POST requests in the log file events.log

# Output
# The function solution should return an integer representing the total number of the successful POST requests found in the events.log

# Running and Testing the Code
# Testing:
# MORE
# Visible Tests: Visible tests can be executed b



# complete the solution below with the question above

# solution.py
# def solution():
#   #implement the solution here
#   return 0

# if __name__ == '__main__':
#    print(solution)





# Expected Output:

# [
#     "/api/v1/orders:6400:3",
#     "/api/v1/users:2560:2", 
#     "/api/v1/products:768:1"
# ]

# Explanation:

# /api/v1/orders: 3 requests, total bytes = 2048 + 2560 + 1792 = 6400
# /api/v1/users: 2 requests, total bytes = 1024 + 1536 = 2560
# /api/v1/products: 1 request, total bytes = 768
# Sorted by request count (descending): 3, 2, 1
# Within same count, sorted lexicographically



# Problem: Calculate the total number of successful POST requests in the log file events.log
# Log Format: [15/Sep/2023:13:25:34 -0400] "POST /upload/file HTTP/1.1" 201 48299

def solution():
    import re
    import os
    
    log_file_path = "/var/logs/events.log"
    successful_post_count = 0
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                # Parse the log line using regex
                match = re.match(r'\[([^\]]+)\] "(\w+) ([^"]+)" (\d+) (\d+)', line.strip())
                if match:
                    method = match.group(2)
                    status_code = int(match.group(4))
                    
                    # Check if it's a POST request with successful status code (200-299)
                    if method == "POST" and 200 <= status_code <= 299:
                        successful_post_count += 1
    
    except FileNotFoundError:
        return 0
    
    return successful_post_count

if __name__ == '__main__':
    print(solution())


# QUESTION 2

# You are working with web server log files located in the /var/logs/ directory. Each log file (e.g., app.log) contains details about HTTP requests made to the server, including the timestamp, request type, file requested, protocol version, status code, and the size of the response in bytes.
# Each log line in the log file is formatted as follows:
# [12/Sep/2023:13:25:34 -0400] "POST /api/v1/resource HTTP/1.1" 201 54321
# WHERE:

# The first part ([12/Sep/2023:13:25:34 -0400]) is the timestamp.
# "POST /api/v1/resource HTTP/1.1" is the request line, including the HTTP method, path requested, and protocol version.
# 201 is the HTTP status code.
# 54321 is the size of the response in bytes.

# Task
# Identify the resources that received successful POST requests recorded in app.log and compute the total number of bytes transferred for each resource. Form a string for each resource alongside its cumulative bytes transferred. Sort the resources first by the number of requests in descending order, and for resources with identical number of requests, sort them lexicographically by path name.
# Output
# The function solution should return the resources that received successful POST requests and the total of bytes transferred for each resource, separated and sorted as described above.
# Return format: List of strings in format "path:total_bytes:request_count"


def solution():
    import re
    from collections import defaultdict
    
    log_file_path = "/var/logs/app.log"
    
    # Dictionary to store resource data: {path: {'bytes': total_bytes, 'count': request_count}}
    resource_data = defaultdict(lambda: {'bytes': 0, 'count': 0})
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                # Parse the log line using regex
                # Pattern: [timestamp] "METHOD path HTTP/version" status_code response_size
                pattern = r'\[([^\]]+)\] "(\w+) ([^"]+) HTTP/[\d\.]+"\s+(\d+)\s+(\d+)'
                match = re.match(pattern, line.strip())
                
                if match:
                    method = match.group(2)
                    path = match.group(3)
                    status_code = int(match.group(4))
                    response_size = int(match.group(5))
                    
                    # Check if it's a successful POST request (status codes 200-299)
                    if method == "POST" and 200 <= status_code <= 299:
                        # Extract just the path without query parameters
                        resource_path = path.split('?')[0] if '?' in path else path
                        
                        # Update resource data
                        resource_data[resource_path]['bytes'] += response_size
                        resource_data[resource_path]['count'] += 1
    
    except FileNotFoundError:
        return []
    
    # Convert to list of tuples for sorting
    resource_list = []
    for path, data in resource_data.items():
        resource_list.append((path, data['bytes'], data['count']))
    
    # Sort by request count (descending), then by path name (lexicographically)
    resource_list.sort(key=lambda x: (-x[2], x[0]))
    
    # Format output as requested: "path:total_bytes:request_count"
    result = []
    for path, total_bytes, request_count in resource_list:
        result.append(f"{path}:{total_bytes}:{request_count}")
    
    return result

if __name__ == '__main__':
    print(solution())






# QUESTION 3




# QUESTION 4 

# You are working with web server log files located in the /var/logs/server/ directory and its subdirectories. Each log file (with .log extension) contains details about HTTP requests made to the server, including the IP address, timestamp, request method, URL, protocol version, status code, and response size.
# Each log line in any of these log files is formatted as follows:
# 192.168.1.10 - - [15/Sep/2021:13:25:34 +0000] "POST /api/info HTTP/1.1" 200 15015
# WHERE:

# 192.168.1.10 is the IP address of the client making the request
# [15/Sep/2021:13:25:34 +0000] is the timestamp
# "POST /api/info HTTP/1.1" is the request line including HTTP method, URL, and protocol version
# 200 is the HTTP status code
# 15015 is the size of the returned object in bytes

# Task
# Your goal is to analyze all .log files within the /var/logs/server/ directory and its subdirectories, identifying IP addresses that have made more than threshold successful POST requests within any 15-minute window between start_date and current_date.
# Define:

# start_date = current_date - duration days
# current_date = 15/Sep/2021:00:00:00 +0000

# Implement a function solution(threshold: int, duration: int) -> List[str] that determines suspicious IP addresses, sorted lexicographically.
# Output
# The output should be a lexicographically sorted list of suspicious IP addresses as strings.




# Function Call: solution(threshold=5, duration=7)

# Expected Output:
# ["192.168.1.100"]

# Explanation:

# IP 192.168.1.100 made 6 successful POST requests within a 15-minute window (10:00-10:14)
# This exceeds the threshold of 5, making it suspicious
# IP 10.0.0.50 only made 2 requests, below the threshold
# Result is sorted lexicographically

def solution(threshold: int, duration: int):
    import os
    import re
    from datetime import datetime, timedelta
    from collections import defaultdict
    
    # Define current_date and start_date
    current_date = datetime.strptime("15/Sep/2021:00:00:00 +0000", "%d/%b/%Y:%H:%M:%S %z")
    start_date = current_date - timedelta(days=duration)
    
    # Directory to search for log files
    log_directory = "/var/logs/server/"
    
    # Dictionary to store requests by IP and time
    ip_requests = defaultdict(list)  # {ip: [(timestamp, method, status), ...]}
    
    # Function to recursively find all .log files
    def find_log_files(directory):
        log_files = []
        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.log'):
                        log_files.append(os.path.join(root, file))
        except OSError:
            pass
        return log_files
    
    # Find all log files
    log_files = find_log_files(log_directory)
    
    # Parse each log file
    for log_file in log_files:
        try:
            with open(log_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Parse log line using regex
                    # Pattern: IP - - [timestamp] "METHOD URL HTTP/version" status size
                    pattern = r'^(\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+\[([^\]]+)\]\s+"(\w+)\s+([^"]+)"\s+(\d+)\s+(\d+)'
                    match = re.match(pattern, line)
                    
                    if match:
                        ip_address = match.group(1)
                        timestamp_str = match.group(2)
                        method = match.group(3)
                        status_code = int(match.group(5))
                        
                        try:
                            # Parse timestamp
                            log_time = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")
                            
                            # Check if within our time range
                            if start_date <= log_time <= current_date:
                                # Check if it's a successful POST request (2xx status codes)
                                if method == "POST" and 200 <= status_code <= 299:
                                    ip_requests[ip_address].append(log_time)
                        
                        except ValueError:
                            # Skip malformed timestamps
                            continue
        
        except (FileNotFoundError, PermissionError):
            # Skip files that can't be read
            continue
    
    # Find suspicious IPs
    suspicious_ips = []
    
    for ip, timestamps in ip_requests.items():
        if len(timestamps) == 0:
            continue
            
        # Sort timestamps for this IP
        timestamps.sort()
        
        # Check for any 15-minute window with more than threshold requests
        for i in range(len(timestamps)):
            window_start = timestamps[i]
            window_end = window_start + timedelta(minutes=15)
            
            # Count requests in this 15-minute window
            count = 0
            for j in range(i, len(timestamps)):
                if timestamps[j] <= window_end:
                    count += 1
                else:
                    break
            
            # If count exceeds threshold, this IP is suspicious
            if count > threshold:
                suspicious_ips.append(ip)
                break  # No need to check more windows for this IP
    
    # Sort lexicographically and return
    return sorted(suspicious_ips)

if __name__ == '__main__':
    # Test with threshold=5, duration=7 (last 7 days)
    result = solution(5, 7)
    for ip in result:
        print(ip)



# QUESTION 5: Error Rate Calculator 

# Problem: Calculate the error rate percentage for all HTTP requests in access.log over the last hour.
# Log Format: 127.0.0.1 - - [01/Jan/2024:12:00:00 +0000] "GET /api/users HTTP/1.1" 404 512
# Task: Return the error rate as a float (4xx and 5xx status codes are errors)
# Solution:

def solution():
    import re
    from datetime import datetime, timedelta
    
    log_file_path = "/var/logs/access.log"
    current_time = datetime.now()
    one_hour_ago = current_time - timedelta(hours=1)
    
    total_requests = 0
    error_requests = 0
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.match(r'(\S+) - - \[([^\]]+)\] "(\w+) ([^"]+)" (\d+) (\d+)', line.strip())
                if match:
                    timestamp_str = match.group(2)
                    status_code = int(match.group(5))
                    
                    # Parse timestamp
                    log_time = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")
                    log_time = log_time.replace(tzinfo=None)  # Remove timezone for comparison
                    
                    if log_time >= one_hour_ago:
                        total_requests += 1
                        if status_code >= 400:
                            error_requests += 1
    
    except (FileNotFoundError, ValueError):
        return 0.0
    
    return (error_requests / total_requests * 100) if total_requests > 0 else 0.0

if __name__ == '__main__':
    print(solution())



# QUESTION 6: Top IP Addresses by Request Count
# Problem: Find the top 5 IP addresses by request count from nginx.log
# Log Format: 192.168.1.100 - - [01/Jan/2024:12:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024
# Task: Return a list of tuples [(ip, count), ...] sorted by count descending
# Solution:

def solution():
    import re
    from collections import Counter
    
    log_file_path = "/var/logs/nginx.log"
    ip_counter = Counter()
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.match(r'(\d+\.\d+\.\d+\.\d+)', line.strip())
                if match:
                    ip_address = match.group(1)
                    ip_counter[ip_address] += 1
    
    except FileNotFoundError:
        return []
    
    return ip_counter.most_common(5)

if __name__ == '__main__':
    print(solution())

# QUESTION 7: Average Response Time Calculator
# Problem: Calculate the average response time for successful requests (200-299) from application.log
# Log Format: 2024-01-01 12:00:00 INFO [RequestHandler] GET /api/data - Status: 200, Response Time: 145ms
# Task: Return average response time in milliseconds as float
# Solution:

def solution():
    import re
    
    log_file_path = "/var/logs/application.log"
    response_times = []
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(r'Status: (\d+), Response Time: (\d+)ms', line)
                if match:
                    status_code = int(match.group(1))
                    response_time = int(match.group(2))
                    
                    if 200 <= status_code <= 299:
                        response_times.append(response_time)
    
    except FileNotFoundError:
        return 0.0
    
    return sum(response_times) / len(response_times) if response_times else 0.0

if __name__ == '__main__':
    print(solution())


# QUESTION 8: Database Connection Pool Monitor
# Problem: Count the number of database connection timeouts in db.log for the current day
# Log Format: 2024-01-01 15:30:45 ERROR [ConnectionPool] Connection timeout after 30s - Pool: users_db
# Task: Return count of timeout errors as integer
# Solution:

def solution():
    import re
    from datetime import datetime
    
    log_file_path = "/var/logs/db.log"
    current_date = datetime.now().strftime("%Y-%m-%d")
    timeout_count = 0
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if current_date in line and "Connection timeout" in line and "ERROR" in line:
                    timeout_count += 1
    
    except FileNotFoundError:
        return 0
    
    return timeout_count

if __name__ == '__main__':
    print(solution())

# QUESTION 9: Memory Usage Alert Parser
# Problem: Parse system.log and find the highest memory usage percentage recorded today
# Log Format: Jan 01 12:00:00 server01 kernel: Memory usage: 85.4% (7.2GB/8.0GB)
# Task: Return highest memory percentage as float
# Solution:

def solution():
    import re
    from datetime import datetime
    
    log_file_path = "/var/logs/system.log"
    current_date = datetime.now().strftime("%b %d")
    max_memory_usage = 0.0
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if current_date in line:
                    match = re.search(r'Memory usage: (\d+\.?\d*)%', line)
                    if match:
                        memory_usage = float(match.group(1))
                        max_memory_usage = max(max_memory_usage, memory_usage)
    
    except FileNotFoundError:
        return 0.0
    
    return max_memory_usage

if __name__ == '__main__':
    print(solution())

# QUESTION 10: Failed Login Attempts by User
# Problem: Count failed SSH login attempts per user from auth.log in the last 24 hours
# Log Format: Jan 01 12:00:00 server sshd[1234]: Failed password for admin from 192.168.1.100 port 22 ssh2
# Task: Return dictionary {username: attempt_count}
# Solution:

def solution():
    import re
    from datetime import datetime, timedelta
    from collections import defaultdict
    
    log_file_path = "/var/logs/auth.log"
    current_year = datetime.now().year
    yesterday = datetime.now() - timedelta(days=1)
    failed_attempts = defaultdict(int)
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(r'(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}).*Failed password for (\w+)', line)
                if match:
                    timestamp_str = match.group(1)
                    username = match.group(2)
                    
                    # Parse timestamp (assuming current year)
                    log_time = datetime.strptime(f"{current_year} {timestamp_str}", "%Y %b %d %H:%M:%S")
                    
                    if log_time >= yesterday:
                        failed_attempts[username] += 1
    
    except (FileNotFoundError, ValueError):
        return {}
    
    return dict(failed_attempts)

if __name__ == '__main__':
    print(solution())

# QUESTION 11: API Endpoint Performance Analysis
# Problem: Find the slowest API endpoint from api.log (response time > 1000ms)
# Log Format: 2024-01-01T12:00:00Z GET /api/v1/users/search?q=test 200 1250ms
# Task: Return the endpoint with highest average response time as string
# Solution:

def solution():
    import re
    from collections import defaultdict
    
    log_file_path = "/var/logs/api.log"
    endpoint_times = defaultdict(list)
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(r'(\w+) (/[^\s]+) (\d+) (\d+)ms', line)
                if match:
                    method = match.group(1)
                    endpoint = match.group(2)
                    response_time = int(match.group(4))
                    
                    if response_time > 1000:
                        endpoint_key = f"{method} {endpoint}"
                        endpoint_times[endpoint_key].append(response_time)
    
    except FileNotFoundError:
        return ""
    
    if not endpoint_times:
        return ""
    
    # Calculate average response time for each endpoint
    avg_times = {}
    for endpoint, times in endpoint_times.items():
        avg_times[endpoint] = sum(times) / len(times)
    
    # Return endpoint with highest average
    return max(avg_times, key=avg_times.get) if avg_times else ""

if __name__ == '__main__':
    print(solution())


# QUESTION 12: Disk Space Alert Counter
# Problem: Count critical disk space alerts (>90% usage) from monitoring.log today
# Log Format: 2024-01-01 14:30:00 CRITICAL [DiskMonitor] /dev/sda1 usage: 95.2% (19.0GB/20.0GB)
# Task: Return count of critical alerts as integer
# Solution:

def solution():
    import re
    from datetime import datetime
    
    log_file_path = "/var/logs/monitoring.log"
    current_date = datetime.now().strftime("%Y-%m-%d")
    critical_count = 0
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if current_date in line and "CRITICAL" in line and "DiskMonitor" in line:
                    match = re.search(r'usage: (\d+\.?\d*)%', line)
                    if match:
                        usage_percent = float(match.group(1))
                        if usage_percent > 90:
                            critical_count += 1
    
    except FileNotFoundError:
        return 0
    
    return critical_count

if __name__ == '__main__':
    print(solution())


# QUESTION 13: Container Restart Analysis
# Problem: Find containers that restarted more than 3 times in docker.log today
# Log Format: 2024-01-01T12:00:00.000Z container restart event container_id=abc123 container_name=web-service
# Task: Return list of container names
# Solution:

def solution():
    import re
    from datetime import datetime
    from collections import Counter
    
    log_file_path = "/var/logs/docker.log"
    current_date = datetime.now().strftime("%Y-%m-%d")
    restart_counter = Counter()
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if current_date in line and "container restart event" in line:
                    match = re.search(r'container_name=(\S+)', line)
                    if match:
                        container_name = match.group(1)
                        restart_counter[container_name] += 1
    
    except FileNotFoundError:
        return []
    
    return [name for name, count in restart_counter.items() if count > 3]

if __name__ == '__main__':
    print(solution())


# QUESTION 14: Load Balancer Health Check Failures
# Problem: Count health check failures per backend server from lb.log in the last hour
# Log Format: 2024-01-01 12:00:00 [HealthCheck] backend-server-01:8080 FAILED - Response timeout
# Task: Return dictionary {server: failure_count}
# Solution:

def solution():
    import re
    from datetime import datetime, timedelta
    from collections import defaultdict
    
    log_file_path = "/var/logs/lb.log"
    current_time = datetime.now()
    one_hour_ago = current_time - timedelta(hours=1)
    failures = defaultdict(int)
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*\[HealthCheck\] (\S+) FAILED', line)
                if match:
                    timestamp_str = match.group(1)
                    server = match.group(2)
                    
                    log_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    
                    if log_time >= one_hour_ago:
                        failures[server] += 1
    
    except (FileNotFoundError, ValueError):
        return {}
    
    return dict(failures)

if __name__ == '__main__':
    print(solution())


# QUESTION 15: Security Event Severity Counter
# Problem: Count security events by severity level from security.log today
# Log Format: 2024-01-01 12:00:00 SEVERITY:HIGH [SecurityAlert] Suspicious login attempt from IP 10.0.0.1
# Task: Return dictionary {severity: count}
# Solution:

def solution():
    import re
    from datetime import datetime
    from collections import defaultdict
    
    log_file_path = "/var/logs/security.log"
    current_date = datetime.now().strftime("%Y-%m-%d")
    severity_counter = defaultdict(int)
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if current_date in line:
                    match = re.search(r'SEVERITY:(\w+)', line)
                    if match:
                        severity = match.group(1)
                        severity_counter[severity] += 1
    
    except FileNotFoundError:
        return {}
    
    return dict(severity_counter)

if __name__ == '__main__':
    print(solution())



# QUESTION 16: Cache Hit Rate Calculator
# Problem: Calculate cache hit rate percentage from cache.log for the last 30 minutes
# Log Format: 2024-01-01 12:00:00 [Cache] Key:user_123 Result:HIT Size:2KB TTL:300s
# 2024-01-01 12:00:01 [Cache] Key:user_456 Result:MISS Size:0KB TTL:0s
# Task: Return hit rate as float percentage
# Solution:

def solution():
    import re
    from datetime import datetime, timedelta
    
    log_file_path = "/var/logs/cache.log"
    current_time = datetime.now()
    thirty_minutes_ago = current_time - timedelta(minutes=30)
    
    total_requests = 0
    cache_hits = 0
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*Result:(HIT|MISS)', line)
                if match:
                    timestamp_str = match.group(1)
                    result = match.group(2)
                    
                    log_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    
                    if log_time >= thirty_minutes_ago:
                        total_requests += 1
                        if result == "HIT":
                            cache_hits += 1
    
    except (FileNotFoundError, ValueError):
        return 0.0
    
    return (cache_hits / total_requests * 100) if total_requests > 0 else 0.0

if __name__ == '__main__':
    print(solution())


# QUESTION 17: Microservice Communication Errors
# Problem: Find services with the most inter-service communication errors from microservices.log
# Log Format: 2024-01-01T12:00:00Z [service-a] ERROR calling service-b: Connection refused
# Task: Return top 3 services with most outbound errors as list of tuples [(service, error_count), ...]
# Solution:

def solution():
    import re
    from collections import Counter
    
    log_file_path = "/var/logs/microservices.log"
    error_counter = Counter()
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(r'\[(\w+-\w+)\] ERROR calling (\w+-\w+):', line)
                if match:
                    calling_service = match.group(1)
                    error_counter[calling_service] += 1
    
    except FileNotFoundError:
        return []
    
    return error_counter.most_common(3)

if __name__ == '__main__':
    print(solution())



# QUESTION 18: Deployment Success Rate
# Problem: Calculate deployment success rate from deployment.log for the current month
# Log Format: 2024-01-01 12:00:00 [Deploy] service=user-api version=v1.2.3 status=SUCCESS duration=120s
# 2024-01-01 12:05:00 [Deploy] service=order-api version=v2.1.0 status=FAILED duration=45s
# Task: Return success rate as float percentage
# Solution:

def solution():
    import re
    from datetime import datetime
    
    log_file_path = "/var/logs/deployment.log"
    current_month = datetime.now().strftime("%Y-%m")
    
    total_deployments = 0
    successful_deployments = 0
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if current_month in line and "[Deploy]" in line:
                    match = re.search(r'status=(SUCCESS|FAILED)', line)
                    if match:
                        status = match.group(1)
                        total_deployments += 1
                        if status == "SUCCESS":
                            successful_deployments += 1
    
    except FileNotFoundError:
        return 0.0
    
    return (successful_deployments / total_deployments * 100) if total_deployments > 0 else 0.0

if __name__ == '__main__':
    print(solution())


# QUESTION 19: Network Latency Analysis
# Problem: Find the 95th percentile network latency from network.log today
# Log Format: 2024-01-01 12:00:00 [NetworkMonitor] ping target=8.8.8.8 latency=25.4ms status=OK
# Task: Return 95th percentile latency as float
# Solution:

def solution():
    import re
    from datetime import datetime
    
    log_file_path = "/var/logs/network.log"
    current_date = datetime.now().strftime("%Y-%m-%d")
    latencies = []
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if current_date in line:
                    match = re.search(r'latency=(\d+\.?\d*)ms', line)
                    if match:
                        latency = float(match.group(1))
                        latencies.append(latency)
    
    except FileNotFoundError:
        return 0.0
    
    if not latencies:
        return 0.0
    
    latencies.sort()
    index = int(0.95 * len(latencies))
    return latencies[min(index, len(latencies) - 1)]

if __name__ == '__main__':
    print(solution())


# QUESTION 20: Thread Pool Exhaustion Detector
# Problem: Count thread pool exhaustion events from app.log in the last 6 hours
# Log Format: 2024-01-01 12:00:00 ERROR [ThreadPool] Pool exhausted: 200/200 threads active, rejecting request
# Task: Return count of exhaustion events as integer
# Solution:

def solution():
    import re
    from datetime import datetime, timedelta
    
    log_file_path = "/var/logs/app.log"
    current_time = datetime.now()
    six_hours_ago = current_time - timedelta(hours=6)
    exhaustion_count = 0
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*Pool exhausted', line)
                if match:
                    timestamp_str = match.group(1)
                    log_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    
                    if log_time >= six_hours_ago:
                        exhaustion_count += 1
    
    except (FileNotFoundError, ValueError):
        return 0
    
    return exhaustion_count

if __name__ == '__main__':
    print(solution())



# QUESTION 21: SSL Certificate Expiry Warnings
# Problem: Extract SSL certificates expiring within 30 days from ssl.log
# Log Format: 2024-01-01 12:00:00 WARNING [SSLMonitor] Certificate for api.example.com expires in 15 days
# Task: Return list of domain names with expiring certificates
# Solution:

def solution():
    import re
    
    log_file_path = "/var/logs/ssl.log"
    expiring_domains = []
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(r'Certificate for (\S+) expires in (\d+) days', line)
                if match:
                    domain = match.group(1)
                    days_until_expiry = int(match.group(2))
                    
                    if days_until_expiry <= 30:
                        expiring_domains.append(domain)
    
    except FileNotFoundError:
        return []
    
    return list(set(expiring_domains))  # Remove duplicates

if __name__ == '__main__':
    print(solution())


# QUESTION 22: Backup Job Status Monitor
# Problem: Find failed backup jobs from backup.log in the last 24 hours
# Log Format: 2024-01-01 02:00:00 [BackupJob] database=users_db status=FAILED error="Disk space insufficient"
# Task: Return list of failed database names
# Solution:

def solution():
    import re
    from datetime import datetime, timedelta
    
    log_file_path = "/var/logs/backup.log"
    current_time = datetime.now()
    twenty_four_hours_ago = current_time - timedelta(hours=24)
    failed_databases = []
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*database=(\w+).*status=FAILED', line)
                if match:
                    timestamp_str = match.group(1)
                    database = match.group(2)
                    
                    log_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                    
                    if log_time >= twenty_four_hours_ago:
                        failed_databases.append(database)
    
    except (FileNotFoundError, ValueError):
        return []
    
    return list(set(failed_databases))  # Remove duplicates

if __name__ == '__main__':
    print(solution())



# QUESTION 23: Request Rate Spike Detector
# Problem: Detect request rate spikes (>1000 requests/minute) from traffic.log
# Log Format: 2024-01-01 12:00:00 [Traffic] requests_per_minute=1250 total_requests=75000
# Task: Return list of timestamps when spikes occurred
# Solution:

def solution():
    import re
    from datetime import datetime
    
    log_file_path = "/var/logs/traffic.log"
    current_date = datetime.now().strftime("%Y-%m-%d")
    spike_timestamps = []
    
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if current_date in line:
                    match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*requests_per_minute=(\d+)', line)
                    if match:
                        timestamp = match.group(1)
                        requests_per_minute = int(match.group(2))
                        
                        if requests_per_minute > 1000:
                            spike_timestamps.append(timestamp)
    
    except FileNotFoundError:
        return []
    
    return spike_timestamps

if __name__ == '__main__':
    print(solution())








 ############################################################################
 # ##########################################################################

 # LOG PASSING QUESTIONS BASICS   


# DevOps/SRE Log Parsing Practice Questions - Beginner Solutions

import re
from datetime import datetime, timedelta
from collections import defaultdict, Counter

# Sample log format: IP - - [timestamp] "METHOD /path HTTP/1.1" status_code response_size
# Example: 192.168.1.10 - - [03/Jun/2025:10:08:47 +0000] "GET /login HTTP/1.1" 200 1024

# ============================================================================
# Question 1: Count All Successful GET Requests
# Write a function that parses the log file and returns the number of 
# successful GET requests. A successful request has status code 200.
# ============================================================================

def count_successful_get_requests():
    count = 0  # Initialize counter
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                # Split the line to extract parts
                parts = line.strip().split()
                if len(parts) >= 9:  # Make sure line has enough parts
                    method = parts[5].replace('"', '')  # Remove quotes from "GET
                    status_code = parts[8]  # Status code position
                    
                    # Check if it's a successful GET request
                    if method == "GET" and status_code == "200":
                        count += 1
    
    except FileNotFoundError:
        return 0
    
    return count

if __name__ == "__main__":
    print("1. Successful GET requests:", count_successful_get_requests())
  
   

# ============================================================================
# Question 2: Top 3 Resources by Request Count
# Write a function to find the top 3 most accessed resources (e.g., /login, /home). 
# Sort by the number of requests in descending order.
# ============================================================================

def top_3_resources():
    resource_count = {}  # Dictionary to store resource counts
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 7:
                    resource = parts[6]  # The /path part of request
                    
                    # Count each resource
                    if resource in resource_count:
                        resource_count[resource] += 1
                    else:
                        resource_count[resource] = 1
    
    except FileNotFoundError:
        return []
    
    # Sort resources by count (highest first) and take top 3
    sorted_resources = sorted(resource_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_resources[:3]  # Return first 3 items

if __name__ == "__main__":
    print("2. Top 3 resources:", top_3_resources())
   


# ============================================================================
# Question 3: Requests per 15-minute Window
# Group the log entries into non-overlapping 15-minute windows and count 
# the number of requests per window.
# ============================================================================

def requests_per_15min_window():
    window_counts = {}  # Dictionary to store counts per window
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                # Use regex to extract timestamp
                match = re.search(r'\[([^\]]+)\]', line)
                if match:
                    timestamp_str = match.group(1)
                    
                    # Parse the timestamp
                    try:
                        # Remove timezone for simplicity
                        time_part = timestamp_str.split(' ')[0]
                        timestamp = datetime.strptime(time_part, '%d/%b/%Y:%H:%M:%S')
                        
                        # Round down to 15-minute window
                        minutes = (timestamp.minute // 15) * 15
                        window_start = timestamp.replace(minute=minutes, second=0)
                        window_key = window_start.strftime('%d/%b/%Y:%H:%M')
                        
                        # Count requests in this window
                        if window_key in window_counts:
                            window_counts[window_key] += 1
                        else:
                            window_counts[window_key] = 1
                    
                    except ValueError:
                        continue  # Skip malformed timestamps
    
    except FileNotFoundError:
        return {}
    
    return window_counts

if __name__ == "__main__":
    print("3. 15-minute windows:", requests_per_15min_window())
   


# ============================================================================
# Question 4: Sort IPs by Total Requests
# Write a function that returns a list of IP addresses sorted by the total 
# number of requests made in descending order.
# ============================================================================

def sort_ips_by_requests():
    ip_counts = {}  # Dictionary to count requests per IP
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 1:
                    ip_address = parts[0]  # First part is always IP
                    
                    # Count requests per IP
                    if ip_address in ip_counts:
                        ip_counts[ip_address] += 1
                    else:
                        ip_counts[ip_address] = 1
    
    except FileNotFoundError:
        return []
    
    # Sort IPs by request count (highest first)
    sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_ips

if __name__ == "__main__":
    print("4. IPs by requests:", sort_ips_by_requests())
    

# ============================================================================
# Question 5: Identify Most Active User Agents
# Identify the top 2 most frequently occurring user agents from the log.
# Note: Assuming extended log format that includes user agent
# ============================================================================

def top_2_user_agents():
    user_agent_counts = {}  # Dictionary to count user agents
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                # Look for user agent in quotes at the end of line
                # Pattern: "User Agent String"
                user_agent_match = re.findall(r'"([^"]*)"', line)
                if len(user_agent_match) >= 2:  # At least request and user agent
                    user_agent = user_agent_match[-1]  # Last quoted string is usually user agent
                    
                    # Skip empty user agents
                    if user_agent and user_agent != '-':
                        if user_agent in user_agent_counts:
                            user_agent_counts[user_agent] += 1
                        else:
                            user_agent_counts[user_agent] = 1
    
    except FileNotFoundError:
        return []
    
    # Sort by count and return top 2
    sorted_agents = sorted(user_agent_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_agents[:2]

if __name__ == "__main__":
    print("5. Top 2 user agents:", top_2_user_agents())
   


# ============================================================================
# Question 6: Count 404 Errors per Endpoint
# Identify the endpoints that resulted in 404 status codes and count 
# how many times each occurred.
# ============================================================================

def count_404_errors_per_endpoint():
    error_404_counts = {}  # Dictionary to count 404s per endpoint
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 9:
                    endpoint = parts[6]  # The /path part
                    status_code = parts[8]  # Status code
                    
                    # Only count 404 errors
                    if status_code == "404":
                        if endpoint in error_404_counts:
                            error_404_counts[endpoint] += 1
                        else:
                            error_404_counts[endpoint] = 1
    
    except FileNotFoundError:
        return {}
    
    return error_404_counts

if __name__ == "__main__":
    print("6. 404 errors per endpoint:", count_404_errors_per_endpoint())
 



# ============================================================================
# Question 7: IPs with More Than 10 Failed Requests in 5 Minutes
# Detect IPs with more than 10 requests returning 4xx or 5xx within 
# any 5-minute window.
# ============================================================================

def ips_with_many_failed_requests():
    ip_requests = defaultdict(list)  # Store all failed requests per IP with timestamps
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 9:
                    ip_address = parts[0]
                    status_code = int(parts[8])
                    
                    # Check if it's a failed request (4xx or 5xx)
                    if status_code >= 400:
                        # Extract timestamp
                        timestamp_match = re.search(r'\[([^\]]+)\]', line)
                        if timestamp_match:
                            timestamp_str = timestamp_match.group(1).split(' ')[0]
                            try:
                                timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
                                ip_requests[ip_address].append(timestamp)
                            except ValueError:
                                continue
    
    except FileNotFoundError:
        return []
    
    suspicious_ips = []
    
    # Check each IP for 5-minute windows with >10 failures
    for ip, timestamps in ip_requests.items():
        timestamps.sort()  # Sort timestamps
        
        # Check sliding 5-minute windows
        for i in range(len(timestamps)):
            window_end = timestamps[i] + timedelta(minutes=5)
            count = 0
            
            # Count failures in this 5-minute window
            for j in range(i, len(timestamps)):
                if timestamps[j] <= window_end:
                    count += 1
                else:
                    break
            
            # If more than 10 failures in 5 minutes, it's suspicious
            if count > 10:
                window_start_str = timestamps[i].strftime('%H:%M')
                window_end_str = window_end.strftime('%H:%M')
                suspicious_ips.append(f"{ip} -> {count} failures ({window_start_str} - {window_end_str})")
                break  # Don't need to check more windows for this IP
    
    return suspicious_ips

if __name__ == "__main__":
    print("7. Suspicious IPs:", ips_with_many_failed_requests())
   



# ============================================================================
# Question 8: Average Number of Bytes Sent per Resource
# Calculate the average number of bytes sent (if available) per resource. 
# Ignore entries with '-' in the bytes field.
# ============================================================================

def average_bytes_per_resource():
    resource_bytes = defaultdict(list)  # Store all byte counts per resource
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 10:
                    resource = parts[6]  # The /path part
                    bytes_sent = parts[9]  # Response size
                    
                    # Skip entries with '-' (no size recorded)
                    if bytes_sent != '-':
                        try:
                            bytes_count = int(bytes_sent)
                            resource_bytes[resource].append(bytes_count)
                        except ValueError:
                            continue  # Skip non-numeric values
    
    except FileNotFoundError:
        return {}
    
    # Calculate averages
    averages = {}
    for resource, byte_list in resource_bytes.items():
        if byte_list:  # Make sure list is not empty
            averages[resource] = sum(byte_list) // len(byte_list)  # Integer division for cleaner output
    
    return averages

if __name__ == "__main__":
    print("8. Average bytes per resource:", average_bytes_per_resource())
  



# ============================================================================
# Question 9: Hour with Peak Traffic
# Determine the hour of the day with the highest number of requests.
# ============================================================================

def hour_with_peak_traffic():
    hour_counts = defaultdict(int)  # Count requests per hour
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                # Extract timestamp
                timestamp_match = re.search(r'\[([^\]]+)\]', line)
                if timestamp_match:
                    timestamp_str = timestamp_match.group(1).split(' ')[0]
                    try:
                        timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
                        hour_key = f"{timestamp.hour:02d}:00 - {timestamp.hour+1:02d}:00"
                        hour_counts[hour_key] += 1
                    except ValueError:
                        continue
    
    except FileNotFoundError:
        return None
    
    if not hour_counts:
        return None
    
    # Find hour with maximum requests
    peak_hour = max(hour_counts.items(), key=lambda x: x[1])
    return f"{peak_hour[0]} -> {peak_hour[1]} requests"

if __name__ == "__main__":
    print("9. Peak traffic hour:", hour_with_peak_traffic())



# ============================================================================
# Question 10: First Request Timestamp per IP
# Find the first request timestamp for each unique IP address.
# ============================================================================

def first_request_per_ip():
    ip_first_request = {}  # Store first timestamp per IP
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 4:
                    ip_address = parts[0]
                    
                    # Extract timestamp
                    timestamp_match = re.search(r'\[([^\]]+)\]', line)
                    if timestamp_match:
                        timestamp_str = timestamp_match.group(1).split(' ')[0]
                        try:
                            timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
                            
                            # Keep only the earliest timestamp for each IP
                            if ip_address not in ip_first_request:
                                ip_first_request[ip_address] = timestamp
                            elif timestamp < ip_first_request[ip_address]:
                                ip_first_request[ip_address] = timestamp
                                
                        except ValueError:
                            continue
    
    except FileNotFoundError:
        return {}
    
    # Convert timestamps to readable format
    result = {}
    for ip, timestamp in ip_first_request.items():
        result[ip] = timestamp.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    
    return result

if __name__ == "__main__":
    print("10. First request per IP:", first_request_per_ip())










    ############################################################################
 # ##########################################################################

 # LOG PASSING QUESTIONS ADVANCE

# Advanced Log Parsing Questions - Beginner-Friendly Solutions

import re
import json
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import statistics

# Sample log format: IP - - [timestamp] "METHOD /path HTTP/1.1" status_code response_size "user_agent"
# Example: 192.168.1.10 - - [03/Jun/2025:10:08:47 +0000] "GET /login HTTP/1.1" 200 1024 "Mozilla/5.0..."

# ============================================================================
# Question 1: Parse Timestamps & Detect Timezone Anomalies
# Task: Check if any logs have timestamps outside the expected UTC timezone (+0000).
# Expected Output: List of dictionaries with IP, timestamp, and timezone info
# ============================================================================

def detect_timezone_anomalies():
    anomalies = []  # List to store timezone anomalies
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 4:
                    ip = parts[0]  # First part is IP address
                    
                    # Find timestamp in brackets [03/Jun/2025:10:08:47 +0000]
                    timestamp_match = re.search(r'\[([^\]]+)\]', line)
                    if timestamp_match:
                        full_timestamp = timestamp_match.group(1)
                        
                        # Split timestamp and timezone
                        if '+' in full_timestamp or '-' in full_timestamp:
                            # Find timezone part (last +XXXX or -XXXX)
                            timezone_match = re.search(r'([+-]\d{4})$', full_timestamp)
                            if timezone_match:
                                timezone = timezone_match.group(1)
                                timestamp_part = full_timestamp.replace(timezone, '').strip()
                                
                                # Convert to ISO format for easier reading
                                try:
                                    dt = datetime.strptime(timestamp_part, '%d/%b/%Y:%H:%M:%S')
                                    iso_timestamp = dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')
                                    
                                    # Check if timezone is not UTC (+0000)
                                    entry = {
                                        "ip": ip,
                                        "timestamp": iso_timestamp,
                                        "timezone": timezone
                                    }
                                    
                                    # Add all entries (both valid and anomalies for comparison)
                                    anomalies.append(entry)
                                    
                                except ValueError:
                                    continue  # Skip malformed timestamps
    
    except FileNotFoundError:
        return []
    
    return anomalies

if __name__ == "__main__":
    print("1. Timezone anomalies:", detect_timezone_anomalies())
   

# ============================================================================
# Question 2: Track User Session Durations
# Task: For each IP, calculate the time difference between first and last request.
# Expected Output: Dictionary with IP as key and duration as "HH:MM:SS" format
# ============================================================================

def track_session_durations():
    ip_timestamps = defaultdict(list)  # Store all timestamps per IP
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 4:
                    ip = parts[0]
                    
                    # Extract timestamp
                    timestamp_match = re.search(r'\[([^\]]+)\]', line)
                    if timestamp_match:
                        timestamp_str = timestamp_match.group(1).split(' ')[0]  # Remove timezone
                        try:
                            timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
                            ip_timestamps[ip].append(timestamp)
                        except ValueError:
                            continue
    
    except FileNotFoundError:
        return {}
    
    # Calculate session durations
    durations = {}
    for ip, timestamps in ip_timestamps.items():
        if len(timestamps) > 1:  # Need at least 2 requests for duration
            timestamps.sort()  # Sort to get first and last
            first_request = timestamps[0]
            last_request = timestamps[-1]
            
            # Calculate duration
            duration = last_request - first_request
            
            # Format as HH:MM:SS
            total_seconds = int(duration.total_seconds())
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            
            durations[ip] = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            # Single request = 0 duration
            durations[ip] = "00:00:00"
    
    return durations

if __name__ == "__main__":
    print("2. Session durations:", track_session_durations())
    

# ============================================================================
# Question 3: Detect Bots/Scrapers by User-Agent
# Task: Flag non-browser UAs (e.g., curl, Python-urllib, Go-http-client).
# Expected Output: Dictionary with bot user agents and their request counts
# ============================================================================

def detect_bots_by_user_agent():
    bot_agents = {}  # Dictionary to count bot user agents
    
    # Common bot/scraper identifiers
    bot_keywords = ['curl', 'python', 'go-http', 'wget', 'bot', 'crawler', 'spider', 'scraper']
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                # Find user agent in quotes (usually last quoted string)
                user_agent_matches = re.findall(r'"([^"]*)"', line)
                if len(user_agent_matches) >= 2:  # Need at least request and user agent
                    user_agent = user_agent_matches[-1]  # Last quoted string
                    
                    # Check if user agent contains bot keywords
                    user_agent_lower = user_agent.lower()
                    is_bot = any(keyword in user_agent_lower for keyword in bot_keywords)
                    
                    if is_bot and user_agent != '-':  # Skip empty user agents
                        # Count this bot user agent
                        if user_agent in bot_agents:
                            bot_agents[user_agent] += 1
                        else:
                            bot_agents[user_agent] = 1
    
    except FileNotFoundError:
        return {}
    
    return bot_agents

if __name__ == "__main__":
    print("3. Bot user agents:", detect_bots_by_user_agent())
    

# ============================================================================
# Question 4: Calculate P99 Latency per Endpoint
# Task: Compute the 99th percentile response time (assuming response time is logged).
# Note: This assumes response time is available in logs (extended format)
# Expected Output: Dictionary with endpoint and P99 latency
# ============================================================================

def calculate_p99_latency():
    endpoint_latencies = defaultdict(list)  # Store latencies per endpoint
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 11:  # Extended log format with response time
                    endpoint = parts[6]  # Path/endpoint
                    
                    # Assuming response time is in the last field (in seconds)
                    try:
                        response_time = float(parts[-1])  # Last field as response time
                        endpoint_latencies[endpoint].append(response_time)
                    except (ValueError, IndexError):
                        continue  # Skip if no valid response time
    
    except FileNotFoundError:
        return {}
    
    # Calculate P99 (99th percentile) for each endpoint
    p99_results = {}
    for endpoint, latencies in endpoint_latencies.items():
        if latencies:  # Make sure we have data
            # Sort latencies to find 99th percentile
            latencies.sort()
            p99_index = int(0.99 * len(latencies))  # 99th percentile index
            p99_value = latencies[min(p99_index, len(latencies) - 1)]
            
            # Format as seconds with 1 decimal place
            p99_results[endpoint] = f"{p99_value:.1f}s"
    
    return p99_results

if __name__ == "__main__":
    print("4. P99 latency:", calculate_p99_latency())
  

# ============================================================================
# Question 5: Identify Traffic Spikes (Rolling 1-min Avg vs Current)
# Task: Compare current requests/min to a 10-min rolling average; flag spikes >50%.
# Expected Output: Dictionary with timestamps showing traffic spikes
# ============================================================================

def identify_traffic_spikes():
    minute_counts = defaultdict(int)  # Count requests per minute
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                # Extract timestamp
                timestamp_match = re.search(r'\[([^\]]+)\]', line)
                if timestamp_match:
                    timestamp_str = timestamp_match.group(1).split(' ')[0]
                    try:
                        timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
                        # Group by minute (ignore seconds)
                        minute_key = timestamp.replace(second=0)
                        minute_counts[minute_key] += 1
                    except ValueError:
                        continue
    
    except FileNotFoundError:
        return {}
    
    # Find spikes by comparing to rolling average
    spikes = {}
    sorted_minutes = sorted(minute_counts.keys())
    
    for i, current_minute in enumerate(sorted_minutes):
        current_count = minute_counts[current_minute]
        
        # Calculate 10-minute rolling average (previous 10 minutes)
        start_index = max(0, i - 10)
        window_counts = [minute_counts[sorted_minutes[j]] for j in range(start_index, i)]
        
        if window_counts:  # Make sure we have historical data
            avg_count = sum(window_counts) / len(window_counts)
            
            # Check if current count is >50% higher than average
            if avg_count > 0 and current_count > avg_count * 1.5:
                deviation = ((current_count - avg_count) / avg_count) * 100
                
                spikes[current_minute.strftime('%Y-%m-%dT%H:%M')] = {
                    "current": current_count,
                    "avg": int(avg_count),
                    "deviation": f"{deviation:.0f}%"
                }
    
    return spikes

if __name__ == "__main__":
    print("5. Traffic spikes:", identify_traffic_spikes())
   

# ============================================================================
# Question 6: Detect Retry Patterns After 5xx Errors
# Task: Find IPs retrying the same path within 5 seconds after a 5xx error.
# Expected Output: Dictionary with IP and retry information
# ============================================================================

def detect_retry_patterns():
    ip_requests = defaultdict(list)  # Store requests per IP
    retry_patterns = {}
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 9:
                    ip = parts[0]
                    path = parts[6]
                    status_code = int(parts[8])
                    
                    # Extract timestamp
                    timestamp_match = re.search(r'\[([^\]]+)\]', line)
                    if timestamp_match:
                        timestamp_str = timestamp_match.group(1).split(' ')[0]
                        try:
                            timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
                            
                            # Store request info
                            ip_requests[ip].append({
                                'timestamp': timestamp,
                                'path': path,
                                'status': status_code
                            })
                        except ValueError:
                            continue
    
    except FileNotFoundError:
        return {}
    
    # Look for retry patterns
    for ip, requests in ip_requests.items():
        requests.sort(key=lambda x: x['timestamp'])  # Sort by time
        
        for i in range(len(requests) - 1):
            current_request = requests[i]
            next_request = requests[i + 1]
            
            # Check if current request was 5xx error
            if (current_request['status'] >= 500 and 
                current_request['path'] == next_request['path']):
                
                # Check if retry happened within 5 seconds
                time_diff = next_request['timestamp'] - current_request['timestamp']
                if time_diff.total_seconds() <= 5:
                    retry_patterns[ip] = {
                        "path": current_request['path'],
                        "first_failure": current_request['timestamp'].strftime('%Y-%m-%dT%H:%M:%S.000Z'),
                        "retry_time": f"{time_diff.total_seconds():.1f}s"
                    }
                    break  # Found retry pattern for this IP
    
    return retry_patterns

if __name__ == "__main__":
    print("6. Retry patterns:", detect_retry_patterns())
    

# ============================================================================
# Question 7: Geolocate IPs & Map Error Rates by Country
# Task: Use a mock GeoIP DB to count 4xx/5xx errors per country.
# Expected Output: Dictionary with country codes and error counts
# ============================================================================

def map_errors_by_country():
    # Mock GeoIP database (in real scenario, you'd use a real GeoIP service)
    mock_geoip = {
        '192.168.1.': 'US',    # Local network = US
        '185.195.': 'DE',      # Some European IP = Germany
        '203.0.': 'AU',        # Some Asian Pacific IP = Australia
        '10.0.': 'US',         # Private network = US
        '172.16.': 'US'        # Private network = US
    }
    
    country_errors = defaultdict(lambda: {'4xx': 0, '5xx': 0})
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 9:
                    ip = parts[0]
                    status_code = int(parts[8])
                    
                    # Simple country lookup based on IP prefix
                    country = 'Unknown'
                    for ip_prefix, country_code in mock_geoip.items():
                        if ip.startswith(ip_prefix):
                            country = country_code
                            break
                    
                    # Count 4xx and 5xx errors
                    if 400 <= status_code < 500:
                        country_errors[country]['4xx'] += 1
                    elif status_code >= 500:
                        country_errors[country]['5xx'] += 1
    
    except FileNotFoundError:
        return {}
    
    # Remove countries with no errors
    return {country: errors for country, errors in country_errors.items() 
            if errors['4xx'] > 0 or errors['5xx'] > 0}

if __name__ == "__main__":
    print("7. Errors by country:", map_errors_by_country())
  

# ============================================================================
# Question 8: Extract Embedded JSON Payloads (If Any)
# Task: If logs contain JSON (e.g., {"user_id": "abc"}), parse and count occurrences.
# Expected Output: Dictionary with key=value pairs and their counts
# ============================================================================

def extract_json_payloads():
    json_data = defaultdict(int)  # Count key=value pairs
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                # Look for JSON patterns in the log line
                json_matches = re.findall(r'\{[^}]+\}', line)
                
                for json_str in json_matches:
                    try:
                        # Parse JSON
                        data = json.loads(json_str)
                        
                        # Extract key=value pairs
                        for key, value in data.items():
                            pair = f"{key}={value}"
                            json_data[pair] += 1
                    
                    except json.JSONDecodeError:
                        continue  # Skip invalid JSON
    
    except FileNotFoundError:
        return {}
    
    return dict(json_data)

if __name__ == "__main__":
    print("8. JSON payloads:", extract_json_payloads())
    

# ============================================================================
# Question 9: Detect Slow Queries (Top 1% by Response Size)
# Task: Identify endpoints with response sizes in the top 1%.
# Expected Output: List of dictionaries with path and bytes_sent
# ============================================================================

def detect_slow_queries():
    endpoint_sizes = []  # Store all response sizes with endpoints
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 10:
                    path = parts[6]
                    response_size = parts[9]
                    
                    # Skip entries with '-' (no size)
                    if response_size != '-':
                        try:
                            size_bytes = int(response_size)
                            endpoint_sizes.append({
                                'path': path,
                                'bytes_sent': size_bytes
                            })
                        except ValueError:
                            continue
    
    except FileNotFoundError:
        return []
    
    if not endpoint_sizes:
        return []
    
    # Sort by response size (largest first)
    endpoint_sizes.sort(key=lambda x: x['bytes_sent'], reverse=True)
    
    # Get top 1% (at least 1 item)
    top_1_percent_count = max(1, len(endpoint_sizes) // 100)
    top_responses = endpoint_sizes[:top_1_percent_count]
    
    return top_responses

if __name__ == "__main__":
    print("9. Slow queries:", detect_slow_queries())

# ============================================================================
# Question 10: Correlate Errors with Deployments (Using a Deployment Log)
# Task: Given a deployment timestamp, check if error rates spiked within 5 mins post-deploy.
# Expected Output: Dictionary with deployment info and error rate changes
# ============================================================================

def correlate_errors_with_deployments():
    # Mock deployment log (in real scenario, read from separate deployment log file)
    deployments = [
        {"id": "Deploy#123", "time": "2025-06-03T10:00:00Z"},
        {"id": "Deploy#124", "time": "2025-06-03T11:30:00Z"}
    ]
    
    # Get all error timestamps from access log
    error_timestamps = []
    
    try:
        with open('/var/logs/access.log', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 9:
                    status_code = int(parts[8])
                    
                    # Count 4xx and 5xx as errors
                    if status_code >= 400:
                        timestamp_match = re.search(r'\[([^\]]+)\]', line)
                        if timestamp_match:
                            timestamp_str = timestamp_match.group(1).split(' ')[0]
                            try:
                                timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
                                error_timestamps.append(timestamp)
                            except ValueError:
                                continue
    
    except FileNotFoundError:
        return {}
    
    # Analyze each deployment
    results = {}
    for deploy in deployments:
        deploy_time = datetime.strptime(deploy['time'], '%Y-%m-%dT%H:%M:%SZ')
        
        # Count errors 5 minutes before and after deployment
        before_window = deploy_time - timedelta(minutes=5)
        after_window = deploy_time + timedelta(minutes=5)
        
        errors_before = sum(1 for t in error_timestamps if before_window <= t < deploy_time)
        errors_after = sum(1 for t in error_timestamps if deploy_time <= t <= after_window)
        
        # Calculate increase percentage
        if errors_before > 0:
            increase = ((errors_after - errors_before) / errors_before) * 100
        else:
            increase = 0 if errors_after == 0 else float('inf')
        
        results[deploy['id']] = {
            "time": deploy['time'],
            "errors_before": errors_before,
            "errors_after": errors_after,
            "increase": f"{increase:.0f}%" if increase != float('inf') else "∞%"
        }
    
    return results

if __name__ == "__main__":
    print("10. Deployment correlation:", correlate_errors_with_deployments())







 ############################################################################
 # ##########################################################################

 # Log Analyzer

# The Log Analyzer is a Python script designed to parse and analyze log files. 
# It provides functionalities to filter logs by timestamp, log level, or message, 
# as well as generate summaries of the logs.

# run it as 
# python3 script.py test.log

# You can also filter logs by timestamp, log level, or message content. Here are some examples:

#    - Filter logs by timestamp range:

#      python3 script.py test.log "2024-06-08 10:00:00" "2024-06-08 10:30:00"

#    - Filter logs by log level:

#      python3 script.py test.log ERROR

#    - Filter logs by message content:

#      python3 script.py test.log "Database connection failed"

#    Replace `"test.log"` with the path to your log file and adjust filtering criteria as needed.


import json
import sys
from datetime import datetime as dt

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_data = self.parse_log_file()

    def parse_log_file(self):
        logs = []
        with open(self.log_file, 'r') as f:
            log_line = f.readline()
            while log_line:
                log = json.loads(log_line)
                for info in log.keys():
                    if info not in ('time', 'level', 'msg'):
                        log['msg'] += f' | {info}: {log[info]}'
                logs.append({
                    'timestamp': self.parse_timestamp(log['time']),
                    'level': log['level'],
                    'message': log['msg']
                })
                log_line = f.readline()
        return logs
    
    def filter_logs_by_timestamp(self, start, end):
        start = self.parse_timestamp(start)
        end = self.parse_timestamp(end)
        filtered_logs = [log for log in self.log_data if start <= log['timestamp'] <= end]
        return filtered_logs

    @staticmethod
    def parse_timestamp(timestamp_str):
        try:
            timestamp = dt.fromisoformat(timestamp_str)
            formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
            return formatted_timestamp
        except ValueError:
            print(f"Invalid timestamp format: {timestamp_str}. Please use ISO format (YYYY-MM-DDTHH:MM:SS)")
            sys.exit(1)

    def filter_logs_by_level(self, level):
        filtered_logs = [log for log in self.log_data if log['level'] == level]
        return filtered_logs
    
    def filter_logs_by_message(self, message):
        filtered_logs = [log for log in self.log_data if message in log['message']]
        return filtered_logs

    def get_logs_summary(self):
        error_logs = self.filter_logs_by_level('ERROR')
        warning_logs = self.filter_logs_by_level('WARNING')
        info_logs = self.filter_logs_by_level('INFO')
        summary = {
            'total_logs': len(self.log_data),
            'error_logs': len(error_logs),
            'warning_logs': len(warning_logs),
            'info_logs': len(info_logs)
        }
        return summary

def main():
    if len(sys.argv) < 2:
        print('Usage: python script.py <log_file> [start_time end_time | log_level | message]')
        sys.exit(1)
    
    log_file = sys.argv[1]
    log_analyzer = LogAnalyzer(log_file)

    if len(sys.argv) == 2:
        summary = log_analyzer.get_logs_summary()
        print('Logs Summary:')
        print(f'Total Logs: {summary["total_logs"]}')
        print(f'Error Logs: {summary["error_logs"]}')
        print(f'Warning Logs: {summary["warning_logs"]}')
        print(f'Info Logs: {summary["info_logs"]}')
    elif len(sys.argv) == 4:
        start = sys.argv[2]
        end = sys.argv[3]
        filtered_logs = log_analyzer.filter_logs_by_timestamp(start, end)
        print('Filtered Logs:')
        for log in filtered_logs:
            print(f'{log["timestamp"]} - {log["level"]}: {log["message"]}')
    elif len(sys.argv) == 3:
        filter_by = sys.argv[2]
        if filter_by.upper() in ['ERROR', 'WARNING', 'INFO']:
            filtered_logs = log_analyzer.filter_logs_by_level(filter_by.upper())
        else:
            filtered_logs = log_analyzer.filter_logs_by_message(filter_by.lower())
        print('Filtered Logs:')
        for log in filtered_logs:
            print(f'{log["timestamp"]} - {log["level"]}: {log["message"]}')

if __name__ == '__main__':
    main()