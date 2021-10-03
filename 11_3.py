class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


inp = input('Введите число: ')
result = []

while inp != 'stop':
    try:
        if not inp.isdigit():
            raise(MyErr('Вы ввели не число'))
    except MyErr as err:
        print(f'Вызвано исключение: {err}')
    else:
        result.append(int(inp))
    finally:
        inp = input('Введите число: ')
else:
    print(f'Массив чисел готов: {result}')