class Road():
    def __init__(self, _length , _width):
        self.volume = _width * _length * 5 * 25

    def __str__(self):
        return f"Потребуется {self.volume / 1000} тонн асфальта"


width = int(input("Введите ширину дороги: "))
length = int(input("Введите длину дороги: "))
road = Road(length,width)
print(road)