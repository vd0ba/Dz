string_user = input('Введите слова через пробел - ')

list_user = string_user.split()
i = 1

while i <= len(list_user):
    temp = list_user[i - 1]
    if len(temp) > 10:
        print(f'{i}) - {temp[:11]}')
    else:
        print(f'{i}) - {temp}')
    i += 1
