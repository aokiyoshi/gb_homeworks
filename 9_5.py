class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Starting draw...')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(f'{title} pen')

    def draw(self):
        print(f'Starting draw with {self.title}. Really? Maybe get a pencil?')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(f'{title} pencil')

    def draw(self):
        print(
            f'Starting draw with {self.title}. Good choise. Do you have an eraser?')


class Handle (Stationery):
    def __init__(self, title):
        super().__init__(f'{title} handle')

    def draw(self):
        print(f'Starting draw with {self.title}. Interesting...')


s = (Stationery('Berlingo'), Pen('Github'), Pencil('Super'), Handle('Office'))

for item in s:
    print('*' * 5, f'Current item: {item.title}')
    item.draw()
