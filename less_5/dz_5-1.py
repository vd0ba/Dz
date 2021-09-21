# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("dz_5-1.txt", "w") as f_obj:
    while True:
        str = input('Введите строку: ')
        if len(str) != 0:
            f_obj.write(str + '\n')
        else:
            break
# проверка на запись
# with open("dz_5-1.txt") as f_obj:
#     for line in f_obj:
#         print(line)
