# Реализовать два небольших скрипта:
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from sys import argv
from itertools import cycle

script_1, list_us, count_us = argv # работает для словвя
count = 0
for i in cycle(list_us):
    if count > int(count_us):
        break
    else:
        print(i)
        count += 1
