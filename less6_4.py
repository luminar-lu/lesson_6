# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop,turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar,WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
class Car():
    def __init__(self,speed=0,color="0",name = "0",is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        if self.speed == 0:
            a = f"Машина {self.name} поехала."
        else:
            a = f"Машина {self.name} разгоняется."
        self.speed += 10
        return a
    def stop(self):
        if self.speed != 0:
            a = f"Машина {self.name} тормозит."
            self.speed -= 10
        else:
            a = f"Машина {self.name} остановилась."
        return a
    def turn_right(self):
        return f"Машина {self.name} повернула направо."
    def turn_left(self):
        return f"Машина {self.name} повернула налево."
    def show_speed(self):
        return f"Текущая скорость машины {self.name} равна {self.speed} "
class TownCar(Car):
    def __init__(self, speed, color, name, ):
        self.speed = speed
        self.color = color
        self.name = name
    def show_speed(self):
        if self.speed > 60:
            a =  f"Текущая скорость машины {self.name} равна {self.speed}. Внимание! Превышение скорости! "
        else:
            a =  f"Текущая скорость машины {self.name} равна {self.speed} "
        return a
class SportCar(Car):
    def __init__(self, speed, color, name, ):
        self.speed = speed
        self.color = color
        self.name = name
class WorkCar(Car):
    def __init__(self, speed, color, name, ):
        self.speed = speed
        self.color = color
        self.name = name
    def show_speed(self):
        if self.speed > 40:
            a =  f"Текущая скорость машины {self.name} равна {self.speed}. Внимание! Превышение скорости! "
        else:
            a =  f"Текущая скорость машины {self.name} равна {self.speed} "
        return a
class PoliceCar(Car):
    def __init__(self, speed, color, name,is_police = True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

# PoliceCar1 = PoliceCar(0,"black", "  NYPD")
# print(PoliceCar1.stop())
# print(PoliceCar1.go())
# print(PoliceCar1.go())
# print(PoliceCar1.go())
# print(PoliceCar1.stop())
# print(PoliceCar1.stop())
# print(PoliceCar1.turn_left())
# print(PoliceCar1.turn_right())
# print(PoliceCar1.show_speed())
# town_car_1 = TownCar(0,"White", "Opel Astra")
# print(town_car_1.go())
# print(town_car_1.go())
# print(town_car_1.go())
# print(town_car_1.go())
# print(town_car_1.go())
# print(town_car_1.show_speed())
# print(town_car_1.go())
# print(town_car_1.show_speed())
# print(town_car_1.go())
# print(town_car_1.show_speed())