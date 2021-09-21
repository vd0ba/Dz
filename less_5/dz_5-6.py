# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно,
# чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему. Вывести словарь на экран.

import re

subj = {}
with open('dz_5-6.txt', 'r', encoding='UTF-8') as f_o:
    for line in f_o:
        item = re.findall('[а-яА-ЯЁё]+', line)
        hour = re.findall('\d+', line)
        count = 0
        for j in hour:
            count += int(j)
        subj[item[0]] = count
print(subj)