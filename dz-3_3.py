# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    return num_1+num_2+num_3-min([num_1, num_2, num_3])


num_1 = int(input('Введите число 1 - '))
num_2 = int(input('Введите число 2 - '))
num_3 = int(input('Введите число 3 - '))
print(my_func(num_1, num_2, num_3))