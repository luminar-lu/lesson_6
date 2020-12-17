# не вызывается словарь в дочернем классе. почему- не разобрался.
class Worker():
    _income_dict = {}
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        Worker._income_dict["wage"] = income
        Worker._income_dict["bonus"] = income * 0.2
        self.income = Worker._income_dict
        # print(self.income)


class Positions(Worker):

    def get_full_name(self):
        self.full_name = self.name + " " + self.surname
        return f'Полное имя {self.full_name}'

    def get_total_income(self):
        self.total_income = self.income("bonus") + self.income("wage")
        return f'{self.total_income()}'



worker_1 = Worker("Jack", "Sparrow", "Capitan", 100)
print(Positions.get_full_name(worker_1))
print(Positions.get_total_income(worker_1))