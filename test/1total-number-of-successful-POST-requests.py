# Problem: Calculate the total number of successful POST requests in the log file events.log
# Log Format: [15/Sep/2023:13:25:34 -0400] "POST /upload/file HTTP/1.1" 201 48299

def solution():
    import re
    import os
     
    log_file_path = "/var/logs/events.log"
    successful_post_count = 0

    try:
        with open(log_file_path, "r") as file:
            for line in file:
                # Use regular expression to match POST requests
                match = re.match(r'\[([^\]+)\]"(\w+)([^"])"(\d+)', line.strip())
                if match:
                    method = match.group(2)
                    status_code = int(match.group(4))

                    # Check if the request was successful (status code 2xx)
                    if method == "POST" and 200 <= status_code <= 299:
                        successful_post_count += 1
    except FileNotFoundError: 
        return 0
    
    return successful_post_count

if __name__ == "__main__":
    print(solution())
           
    
