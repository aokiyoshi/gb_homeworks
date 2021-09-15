from sys import argv


args = argv

if len(args) == 2:
    values = args[1].split('.')
    if len(values) == 1:
        values.append('0')
    if not values[0]:
        values[0] = '0'
    if not values[1]:
        values[1] = '0'
    if values[0].isdigit() and values[1].isdigit(): 
        result = (f'{values[0]}.{values[1]}').ljust(16)
    with open('6_6/bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(f'{result}\n')
