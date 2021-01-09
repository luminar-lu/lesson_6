# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
class Stationery():
    def __init__(self, title = ""):
        self.title = title
    def draw(self):
        print("Начинаем рисунок.")
class Pen(Stationery):
    def __init__(self, title = ""):
        self.title = title
    def draw(self):
        print(f"Отрисовка контура с помощью {self.title}.")
class Pencil(Stationery):
    def __init__(self, title = ""):
        self.title = title
    def draw(self):
        print(f"Прорисовка теней  с помощью {self.title}.")
class Handle(Stationery):
    def __init__(self, title = ""):
        self.title = title
    def draw(self):
        print(f"Добавление цвета  с помощью {self.title}.")

a = Stationery()
b = Pen("синей ручки ")
c = Pencil("простого карандаша 1Н")
d = Handle("зеленого маркера")
a.draw()
b.draw()
c.draw()
d.draw()


