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