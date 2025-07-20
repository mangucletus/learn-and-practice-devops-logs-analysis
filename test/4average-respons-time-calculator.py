# Problem: Calculate the average response time for successful requests (200-299) from application.log
# Log Format: 2024-01-01 12:00:00 INFO [RequestHandler] GET /api/data - Status: 200, Response Time: 145ms

# Task: Return average response time in milliseconds as float

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