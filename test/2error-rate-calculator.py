# Problem: Calculate the error rate percentage for all HTTP requests in access.log over the last hour.
# Log Format: 127.0.0.1 - - [01/Jan/2024:12:00:00 +0000] "GET /api/users HTTP/1.1" 404 512

# Task: Return the error rate as a float (4xx and 5xx status codes are errors)

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