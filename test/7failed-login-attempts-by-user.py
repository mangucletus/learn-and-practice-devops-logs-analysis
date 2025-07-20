# Problem: Count failed SSH login attempts per user from auth.log in the last 24 hours
# Log Format: Jan 01 12:00:00 server sshd[1234]: Failed password for admin from 192.168.1.100 port 22 ssh2
# Task: Return dictionary {username: attempt_count}

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