# Problem: Find the top 5 IP addresses by request count from nginx.log
# Log Format: 192.168.1.100 - - [01/Jan/2024:12:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024

# Task: Return a list of tuples [(ip, count), ...] sorted by count descending 

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