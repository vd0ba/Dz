list_1 = input('Введите данные через пробел: ')
list_1 = list_1.split()
i = 0

while i < len(list_1):
    if i % 2 != 0:
        list_1[i], list_1[i - 1] = list_1[i - 1], list_1[i]
    i += 1
print(list_1)
