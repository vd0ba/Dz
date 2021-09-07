num_month = input('Введите число месяца: ')

if num_month.isdigit():
    num_month = int(num_month)
else:
    print('ERROR')

# через list
# months = ['Зима', 'Весна', 'Лето', 'Осень']
# if num_month in (1,2,12):
#     print(months[0])
# elif num_month in (3,4,5):
#     print(months[1])
# elif num_month in (6,7,8):
#     print(months[2])
# elif num_month in (9,10,11):
#     print(months[3])
# else:
#     print('Некорректное число')

# 2 через dict
dict_month = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
if 0<num_month <13:
    for key, value in dict_month.items():
        if num_month in value:
            print(key)
else:
    print('Некорректное число')