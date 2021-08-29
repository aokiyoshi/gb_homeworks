def sum_of_digits(num):
    summ = 0
    while num:
        digit = num % 10
        num = num // 10
        summ += digit
    return summ

cubes = [x*x*x for x in range(1, 1000) if x % 2 != 0]
summ = 0
for i in cubes:
    if sum_of_digits(i) % 7 == 0:
        summ += i 

print(summ)

cubes = [x ** 3 + 17 for x in range(1, 1000) if x % 2 != 0]
summ = 0
summ = 0
for i in cubes:
    if sum_of_digits(i) % 7 == 0:
        summ += i 

print(summ)

print(sum([num for num in [n ** 3 for n in range(1, 1000)  if n % 2 != 0]
          if sum([int(i) for i in list(str(num))]) % 7 == 0]))

print(sum([num for num in [n ** 3 + 17 for n in range(1, 1000) if n % 2 != 0]
          if sum([int(i) for i in list(str(num))]) % 7 == 0]))
