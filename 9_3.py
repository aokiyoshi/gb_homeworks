income = {
    'engineer': {'wage': 2000, 'bonus': 250},
    'cleaner': {'wage': 1000, 'bonus': 100},
    'developer': {'wage': 3000, 'bonus': 250},
}


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position.lower()
        self._income = income[self.position]['wage'] + \
            income[self.position]['bonus']


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income


pos1 = Position('John', 'Smith', 'Engineer')
print(pos1.get_full_name())
print(pos1.get_total_income())
