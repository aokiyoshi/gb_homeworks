from time import sleep
from enum import Enum

class Color(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

    def next(self):
        idx = self.value + 1
        if idx > 3:
            idx = 1
        return Color(idx)

class TrafficLight:
    color = Color.RED

    timings = (7,3,2)

    def running(self):
        while True:
            print(self.color.name)
            self.color = self.color.next()
            sleep(self.timings[self.color.value - 1])

tl = TrafficLight()
tl.running()