from sys import argv


args = argv

if len(args) == 1:
    with open('6_6/bakery.csv', 'r') as f:
        print(f.read())
elif len(args) == 2:
    if not args[1].isdigit():
        print('Неправильный номер строки!')
        exit()
    with open('6_6/bakery.csv', 'r+') as f:
        position = int(args[1])*18 - 18
        f.seek(position)
        if len(f.read()) == 0:
            print('Нет такой записи!')
            exit()
        f.seek(position)
        print(f.read())
