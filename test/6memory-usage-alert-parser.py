# Problem: Parse system.log and find the highest memory usage percentage recorded today
# Log Format: Jan 01 12:00:00 server01 kernel: Memory usage: 85.4% (7.2GB/8.0GB)
# Task: Return highest memory percentage as float

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