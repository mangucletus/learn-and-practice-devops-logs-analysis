# Problem: Count the number of database connection timeouts in db.log for the current day
# Log Format: 2024-01-01 15:30:45 ERROR [ConnectionPool] Connection timeout after 30s - Pool: users_db

# Task: Return count of timeout errors as integer

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
