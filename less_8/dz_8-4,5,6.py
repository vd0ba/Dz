# №4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# №5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# №6.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
class Warehouse:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def show_wh(self):
        print('На складе остались:')
        for key, value in self.items.items():
            print(f'{key} - {value} шт')

    def add_wh(self, equip, count):
        try:
            self.items.update({str(equip): int(count)})
        except ValueError:
            print('Ошибка ввода данных')
        return f'Добавили на склад {equip} в количестве {count} шт'

    def move(self, equip, depart, count):
        equip_count = self.items.get(equip)
        if equip_count is not None:
            try:
                equip_count -= int(count)
                self.items.update({str(equip): equip_count})
            except ValueError:
                print('Ошибка ввода данных')
        return f'Переместили со склада {equip} в количестве {count} шт в отдел {depart}'


class OffEquip:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = int(year)


class Printer(OffEquip):
    def __init__(self, name, color, year, colory):
        super().__init__(name, color, year)
        self.colory = colory

    def action(self):
        print('Печатает')


class Scaner(OffEquip):
    def __init__(self, name, color, year, size):
        super().__init__(name, color, year)
        self.size = size

    def action(self):
        print('Сканирует')


class Xerox(OffEquip):
    def __init__(self, name, color, year, speed):
        super().__init__(name, color, year)
        self.speed = speed

    def action(self):
        print('Копирует')


whouse = Warehouse('Moscow')
printer = Printer('HP 322M', 'white', 2020, 'multi')
whouse.add_wh(printer, 2)
scaner = Scaner('Dell 13', 'blue', 2018, 'A3')
whouse.add_wh(scaner, 1)
xerox = Xerox('Xerox 1', 'gray', 1998, 2)
whouse.add_wh(xerox, 1)
printer = Printer('HP 323M', 'white', 2020, 'monotone')
whouse.add_wh(printer, 1)
whouse.move('HP 323M', 'IT', 1)
whouse.show_wh()
