class Car:
    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print('Wrum wrum')

    def stop(self):
        self.speed = 0
        print('Car stopped')

    def turn(self, direction):
        print('Turning to {direction} degree...')

    def show_speed(self):
        print(f'Current speed is {self.speed}')

    def say_my_name(self):
        print(f'This car has name {self.name}')


class TownCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Over speed!')
        return super().show_speed()


class WorkCar(Car):
    def __init__(self, color, name, is_police=False):
        super().__init__(color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Over speed!')
        return super().show_speed()


cars = (Car('Blue', 'Toyota', is_police=True), TownCar(
    'Green', 'Mazda'), WorkCar('White', 'Nissan'))

for car in cars:
    print('*' * 10)
    car.say_my_name()
    car.go(150)
    car.turn(30)
    car.show_speed()
    car.stop()
    car.show_speed()
