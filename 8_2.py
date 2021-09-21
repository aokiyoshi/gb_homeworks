import re

def parse_logs(log_file_name: str, n: int = 0) -> list:
    i = 0
    result = []
    log_file = open(log_file_name, 'r')
    log_line = log_file.readline()
    while log_line and (n == 0 or i < n):
        ip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}').findall(log_line)[0]
        # If IPv4 not found try to find IPv6
        if ip is None:
            ip = re.compile(r'(\w{3,4}:){7}\w{3,4}').findall(log_line)[0]

        date = re.compile(r'\[(.*?)\]').findall(log_line)[0]
        type = re.compile(r'\"(.*?)\s\/').findall(log_line)[0]
        path = re.compile(r'\".+\s(\/.*?)\s').findall(log_line)[0]

        # This returns tuple with 2 strings, unpack here 
        code, size = re.compile(r'\"\s(\d{3})\s(\d+)').findall(log_line)[0]
        result.append((ip, date, type, path, code, size))
        i += 1
        log_line = log_file.readline() 
        
    log_file.close()
    return result


print(*parse_logs('nginx_logs.txt', n = 10), sep='\n')

