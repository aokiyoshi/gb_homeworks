from itertools import zip_longest


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix(
            [[v1 + v2 for v1, v2 in zip_longest(row1, row2, fillvalue=0)]
             for row1, row2 in zip_longest(self.matrix, other.matrix, fillvalue=[0])]
        )

    def _sub__(self, other):
        return Matrix(
            [[v1 - v2 for v1, v2 in zip_longest(row1, row2, fillvalue=0)]
             for row1, row2 in zip_longest(self.matrix, other.matrix, fillvalue=[0])]
        )

    def __str__(self) -> str:
        return '\n'.join(
            (
                '|' + ' '.join((str(val) for val in row)) + '|' for row in self.matrix
            )
        )


m1 = Matrix([[5, 1, 1], [1, 1, 1], [1, 0, 1]])
m2 = Matrix([[2, 2], [2, 2]])

print(m1)
print(m2)
print(m1 + m2)
