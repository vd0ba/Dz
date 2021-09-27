# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} начала движение')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}')

    def stop(self):
        print(f'{self.color} {self.name} остановилась')

    def show_speed(self):
        print(f'{self.color} {self.name} движется со скоростью {self.speed}')

    def is_pl(self):
        if self.is_police:
            print('Это полицейская машина')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        else:
            print(f'{self.color} {self.name} движется со скоростью {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
        else:
            print(f'{self.color} {self.name} движется со скоростью {self.speed}')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town = TownCar(61, 'белая', 'A')
town.go(), town.is_pl(), town.show_speed(), town.turn('налево'), town.stop()

sport = SportCar(100, 'красная', 'В')
sport.go(), sport.is_pl(), sport.show_speed(), sport.turn('направо'), sport.stop()

work = WorkCar(45, 'желтая', 'С')
work.go(), work.is_pl(), work.show_speed(), work.turn('направо'), work.stop()

police = PoliceCar(100, 'бело-синняя', 'Д', True)
police.go(), police.is_pl(), police.show_speed(), police.turn('налево'), police.stop()
