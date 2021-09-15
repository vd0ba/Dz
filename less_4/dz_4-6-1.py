#  Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
from sys import argv
from itertools import count

script_1, first_num, last_num = argv
for i in count(int(first_num)):
    if i > int(last_num):
        break
    else:
        print(i)