from sys import argv


args = argv

if len(args) == 3:
    if not args[1].isdigit():
        print('Неверный номер строки')
        exit()
    values = args[2].split('.')
    if len(values) == 1:
        values.append('0')
    if not values[0]:
        values[0] = '0'
    if not values[1]:
        values[1] = '0'
    if values[0].isdigit() and values[1].isdigit():
        result = (f'{values[0]}.{values[1]}').ljust(16)
        # Небольшой костыль: каждая строка содержит 16 знаков, недостающее дописывается.
    with open('6_6/bakery.csv', 'r+', encoding='utf-8') as f:
        position = int(args[1])*18 - 18 #Перемещаемся по строкам с учетом того, что все строки по 16 знаком +\n
        f.seek(position)
        if len(f.read()) == 0:
            print('Нет такой записи!')
            exit()
        f.seek(position)
        f.writelines(f'{result}\n')
else:
    print('Неправильное количество аргументов')
