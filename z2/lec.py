# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите натуральное число N = "))
N = number
f = []
for i in range(2, int(number ** 0.5) + 2):
    while number % i == 0:
        f.append(i)
        number //= i
if number != 1:
    f.append(number)
    print(f'Список простых множителей числа {N}: {f}')