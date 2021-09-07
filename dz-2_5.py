list_user = [5, 4, 3, 2, 1]

while True:
    temp = input('Введите число или stop - ')
    if temp.isdigit():
        temp = int(temp)
        ind = None
        for i in list_user:
            if temp > i:
                ind = list_user.index(i)
                break
        if ind == None:
            list_user.append(temp)
        else:
            list_user.insert(ind, temp)
        print(list_user)
    elif temp == 'stop':
        break
    else:
        print('Некорректный ввод')
