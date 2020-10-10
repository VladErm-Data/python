# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
#  зеленый.
# Доп условие я не понял, поэтому не сделал.
from itertools import islice, cycle
import time

TRAFFIC_COLORS = {'Красный': 7, 'Желтый': 2, 'Зеленый': 3}


class TrafficLight:
    def __init__(self, color):
        self.__color = islice(cycle(TRAFFIC_COLORS.keys()), list(TRAFFIC_COLORS.keys()).index(color), None)

    def running(self, block):
        for index, color in enumerate(self.__color):
            if index == block:
                break
            print(color)
            time.sleep(TRAFFIC_COLORS[color])


my_traffic = TrafficLight('Желтый')
my_traffic.running(7)

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, mass, dense):
        print(self._width*self._length*mass*dense)


my_road = Road(5000, 20)
my_road.asphalt_mass(25, 5)

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


ex_1 = Position('Евкакий', 'Самородный', 'Гендир', 10, 5)
print(ex_1.position)
print(ex_1.get_full_name())
print(ex_1.get_total_income())

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f'текущая скорость: {self.speed}'

    @staticmethod
    def go():
        return 'Она поехала'

    @staticmethod
    def stop():
        return 'Она остановилась'

    @staticmethod
    def turn(direction):
        return f'мы повернули на{direction}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            return f'текущая скорость: {self.speed}'
        else:
            return f'превышение скорости! Скорость: {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 40:
            return f'текущая скорость: {self.speed}'
        else:
            return f'превышение скорости! Скорость: {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car_1 = WorkCar(70, 'Blue', 'Toyota', False)
car_2 = SportCar(100, 'Black', 'Bugatti', False)
car_3 = PoliceCar(80, 'Brown', 'Kopeyka', True)
car_4 = TownCar(50, 'White', 'Ford', False)

print(car_1.show_speed())
print(car_2.show_speed())
print(car_3.show_speed())
print(car_4.show_speed())

print(car_3.name)

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.


class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    @staticmethod
    def draw():
        print('Рисуем ручкой')


class Pencil(Stationery):
    @staticmethod
    def draw():
        return print('Рисуем карандашом')


class Handle(Stationery):
    @staticmethod
    def draw():
        return print('Рисуем маркером')


ex_1 = Pen('Ручка')
print(ex_1.title)
ex_1.draw()

ex_2 = Pencil('Карандаш')
print(ex_2.title)
ex_2.draw()
