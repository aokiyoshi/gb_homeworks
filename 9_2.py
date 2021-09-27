class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calc_mass(self):
        return self._lenght * self._width * 25 * 5 / 1000


road_1 = Road(5000, 20)
print(f'Mass of road is {road_1.calc_mass()} tons')
