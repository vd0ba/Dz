# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("dz_5-5.txt", "w") as f_o:
    while True:
        str = input('Введите набор чисел, разделяя пробелом: ')
        if len(str) != 0:
            f_o.write(str + '\n')
        else:
            break
count = 0
with open("dz_5-5.txt") as f_o:
    for line in f_o:
        num_ls = line.split()
        for i in num_ls:
            count += float(i)
    print(f'Сумма чисел в файле - {count}')