# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.

def int_func(str):
    str_ref = str.capitalize()
    return str_ref


#  print(int_func('stroka'))

list_str = input('Введите строку, разделяя слова пробелами - ').split()
for i in range(len(list_str)):
    list_str[i] = int_func(list_str[i])
print(' '.join(list_str))