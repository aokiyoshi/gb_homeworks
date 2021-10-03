class MyDivByZeroError(Exception):
    def __init__(self, text):
        self.text = text


a = input('Введите делимое число: ')
b = input('Введите делитель: ')

try:
    x, y = int(a), int(b)
    if y == 0:
        raise MyDivByZeroError('Вы пытаетесь поделить на ноль!')
except ValueError:
    print('Вы ввели не число')
except MyDivByZeroError as err:
    print(err)
else:
    print(f'Частное равно: {x / y}')
finally:
    print(f'Работа программы завершена')  
