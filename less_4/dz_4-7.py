# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
# функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.

# def fact(n):                  факториал с 0
#     res = 1
#     for i in range(n):
#         for j in range(i+1):
#             if j == 0:
#                 res = 1
#             else:
#                 res *= j
#         print(i,'!= ', end='')
#         yield res

from math import factorial


def fact(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)


num = int(input('Введите число - '))
for i in fact(num + 1):
    print(i)
