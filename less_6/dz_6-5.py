# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen
# (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода
# draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов
# и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationary):
    def draw(self):
        print(f'Запуск отрисовки {self.title}, синий цвет')
class Pencil(Stationary):
    def draw(self):
        print(f'Запуск отрисовки {self.title}, серый цвет')
class Handle(Stationary):
    def draw(self):
        print(f'Запуск отрисовки {self.title}, черный цвет')

st1 = Stationary('Мел')
st1.draw()
st2 = Pen('Ручка')
st2.draw()
st3 = Pencil('Карандаш')
st3.draw()
st4 = Handle('Маркер')
st4.draw()
