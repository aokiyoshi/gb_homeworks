def format_duration(duration):
    days = duration // 86_400
    rem = duration % 86_400
    hours = rem // 3_600
    rem = rem % 3_600
    minutes = rem // 60
    seconds = rem % 60
    return f'{days} д, {hours} ч, {minutes} мин, {seconds} с.'


print(format_duration(12345))