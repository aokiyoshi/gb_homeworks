price_lst = [57.8, 46.51, 97, 300, 250, 75, 0.5, 1.75]

# Выводим цены в виде рублей и копеек
for p in price_lst:
    print(f'{p//1:02.0f} руб {100 * (p % 1):02.0f} коп')

# Сортируем список так, чтобы не создавался новый
print(f'ID списка: {id(price_lst)}')
price_lst.sort()

# Снова выводим цены
print()
for p in price_lst:
    print(f'{p//1:02.0f} руб {100 * (p % 1):02.0f} коп')
print(f'ID списка: {id(price_lst)}')

# Создаем новый список, отсортированный по убываню
rever_lst = reversed(price_lst)

# Снова выводим цены
print()
for p in rever_lst:
    print(f'{p//1:02.0f} руб {100 * (p % 1):02.0f} коп')
print(f'ID списка: {id(rever_lst)}')
