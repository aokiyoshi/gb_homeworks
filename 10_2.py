from abc import ABC, abstractclassmethod


class Cloth(ABC):

    def __init__(self, size):
        self.size = size

    @abstractclassmethod
    def calc_cloth_consum(self):
        pass


class Coat(Cloth):

    @property
    def calc_cloth_consum(self):
        return self.size / 6.5 + 0.5


class Costume(Cloth):

    @property
    def calc_cloth_consum(self):
        return self.size * 2 + 0.3


clothes = (Coat(1), Costume(2))

for cl in clothes:
    print(cl.calc_cloth_consum)
