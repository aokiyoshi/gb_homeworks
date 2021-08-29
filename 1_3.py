def format_procent(num):
    if num % 10 == 1:
        return f"{num} процент"
    elif 20 > num > 10:
        return f"{num} процентов"
    elif num % 10 in (2, 3, 4):
        return f"{num} процента"
    else:
        return f"{num} процентов"


print(format_procent(1))
print(format_procent(25))
print(format_procent(93))
print(format_procent(41))
print(format_procent(10))
