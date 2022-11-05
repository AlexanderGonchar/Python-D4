# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('f1.txt', 'w', encoding='utf-8') as file:
    file.write('1*x^2 + 3*x^4')
with open('f2.txt', 'w', encoding='utf-8') as file:
    file.write('55*x^6 + 7*x^8')

with open('f1.txt','r') as file:
    d1 = file.readline()
    list_of_d1 = d1.split()

with open('f2.txt','r') as file:
    d2 = file.readline()
    list_of_d2 = d2.split()

print(f'{list_of_d1} + {list_of_d2}')
sum_poly = list_of_d1 + list_of_d2

with open('fsum.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_d1} + {list_of_d2}')