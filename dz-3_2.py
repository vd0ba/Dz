#  Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
#  год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
#  Реализовать вывод данных о пользователе одной строкой.

def print_user_inf(name, surname, birth, city, email, telephone):
    print (f'Имя: {name}; Фамилия: {surname}; Год рождения: {birth}; Город: {city}'
           f'Эл.почта: {email}; Телефон: {telephone}')


print_user_inf(name='Vadim', surname='Tt', birth=1993, city='Msc', email='e@mail', telephone=8910)
