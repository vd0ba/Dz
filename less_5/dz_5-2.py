# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

count_line = 0
with open('dz_5-2.txt') as f_o:
    for line in f_o:
        count_line += 1
        str = line.split()
        print(f'Количество слов в {count_line} строке - {len(str)}')
print(f'Количество строк в файле - {count_line}')
