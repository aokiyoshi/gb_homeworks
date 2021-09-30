class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        """Returns sub of 2 cells counts. Returns None and print error message when result is equals to zero or lower than zero"""
        return Cell(self.count - other.count if self.count > other.count else print('Клетка может уничтожится, оператор неприменим'))

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __floordiv__(self, other):
        return Cell(self.count // other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def __str__(self) -> str:
        return str(self.count)

    def make_order(self, n: int) -> str:
        row_num = self.count // n
        rem = int(self.count % n)
        return ('*' * n + '\n') * (row_num - 1) + ('*' * n) + ('\n' if rem != 0 else '') + ('*' * rem)

    def make_order2(self, n: int) -> str:
        row_num = self.count // n
        rem = int(self.count % n)
        return '\n'.join(['*' * n] * row_num) + ('\n' if rem != 0 else '') + ('*' * rem)


c1 = Cell(5)
c2 = Cell(6)
c3 = Cell(25)

print(*(c1 + c2, c2 - c1, c1 - c2, c2 // c1, c3 / c2, c1 *
      c2, c3.make_order(4), c3.make_order2(4)), sep='\n')
