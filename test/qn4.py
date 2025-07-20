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