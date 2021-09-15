from json import dumps


def parse_logs(log_file_name: str, n: int = 0) -> list:
    """
    Функция возвращает список из кортежей вида:\n
    (<remote_addr>, <request_type>, <requested_resource>),\n
    где <remote_addr> - ip-адресс клиента,\n
        <request_type> - вид запроса,\n
        <requested_resource> - ресурс\n
    Параметры:\n
    n(int): сколько строк с файла считать\n
    Возвращаемое значение:\n
    tuple(str, str, str)\n
    """
    result = []
    i = 0
    log_file = open(log_file_name, 'r')
    log_line = log_file.readline()
    while log_line and (n == 0 or i < n):
        logs = log_line.split(' ')
        remote_addr = logs[0]
        request_type = logs[5].replace('"', '')
        requested_resource = logs[6]
        log_line = log_file.readline()
        result.append((remote_addr, request_type, requested_resource))
        i += 1
    log_file.close()
    return result


def get_spamers(log_file_name: str, n: int = 0, criterion: int = 500) -> dict:
    """
    Функция возвращает список спамеров в виде словаря из заданного лог файла \n
    Параметры:\n
    log_file_name(str): имя файла или полный путь к нему \n
    n(int): количество просматриваемых строк, по умолчанию равен нулю и тогда, читаются все строки \n
    criterion(int): какое число сообщений считать спамом \n
    Возвращаемое значение: \n
    dict \n
    """
    users = {}
    spamers = {}
    i = 0
    log_file = open(log_file_name, 'r')
    log_line = log_file.readline()
    while log_line and (n == 0 or i < n):
        logs = log_line.split(' ')
        remote_addr = logs[0]
        log_line = log_file.readline()
        users.setdefault(remote_addr, 0)
        users[remote_addr] += 1
        if users[remote_addr] > 500:
            spamers.setdefault(remote_addr, 0)
            spamers[remote_addr] = users[remote_addr]
        i += 1
    log_file.close()
    return spamers

logs = 'data/nginx_logs.txt'
print(*parse_logs('data/nginx_logs.txt', n=10), sep='\n')
print(dumps(get_spamers('data/nginx_logs.txt', criterion=1000), sort_keys=True, indent=2))
