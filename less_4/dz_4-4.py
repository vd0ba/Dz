# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив
# чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения
# задания обязательно использовать генератор.
list_us = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(list_us)
ord_list = [i for i in list_us if list_us.count(i) == 1]
print(ord_list)
