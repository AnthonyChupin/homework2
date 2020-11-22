"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
       print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction=None):
        print('Машина повернула на ', direction)

    def show_speed(self):
        print('Скорость машины: ', self.speed)

    def get_status(self):
        if self.is_police:
            print('Это полицейская машина')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышена скорость! ','Скорость машины: ', self.speed)
        else:
            print('Скорость машины: ', self.speed)


class SportCar(Car):
    def get_status(self):
        print('Это спортивная машина')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышена скорость! ', 'Скорость машины: ', self.speed)
        else:
            print('Скорость машины: ', self.speed)


class PoliceCar(Car):
    def sirena(self):
        print('Сирена включена')


town_car = TownCar(65, 'red', 'kia', False)
sport_car = SportCar(120, 'blak', 'ferrari', False)
police_car = PoliceCar(70, 'green', 'ford', True)
work_car = WorkCar(41, 'yellow', 'kamaz', False)

print(town_car.name, ' ', town_car.color,)
town_car.show_speed()
town_car.get_status()
town_car.stop()
print('----------------------------')

print(sport_car.name, ' ', sport_car.color,)
sport_car.show_speed()
sport_car.get_status()
sport_car.go()
print('----------------------------')

print(police_car.name, ' ', police_car.color,)
police_car.show_speed()
police_car.get_status()
police_car.turn('право')
print('----------------------------')

print(work_car.name, ' ', work_car.color,)
work_car.show_speed()
work_car.get_status()
work_car.turn('лево')
print('----------------------------')



