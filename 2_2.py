list_1 = ['в', '5', 'часов', '17', 'минут',
          'температура', 'воздуха', 'была', '+5', 'градусов']

for i, element in enumerate(list_1):
    sign = element[0] if element[0] in ('+', '-') else ''
    no_plus_minus = element.replace('+', '').replace('-', '')
    if no_plus_minus.isdigit():
        list_1[i] = f'"{sign}{int(no_plus_minus):02d}"'

print(' '.join(list_1))
