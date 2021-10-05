# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.

class Data:
    def __init__(self, data_string):
        self.data_string = data_string

    @classmethod
    def str_int(cls, data_string):
        return list(map(int, data_string.split('-')))

    @staticmethod
    def is_data(data_string):
        day, month, year = map(int, data_string.split('-'))
        if day < 0 or day > 31:
            print('Такого дня не существует')
        if day < 0 or month > 12:
            print('Такого месяца не существует')
        if year < 0 or year > 2021:
            print('Такого года не существует')

print(Data.str_int('03-10-2021'))
Data.is_data('03-13-2222')