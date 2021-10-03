class ComplexNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNum(self.re * other.re, self.im * other.im)

    def turn_90(self):
        return ComplexNum(-self.im, self.re)

    @property
    def modulus(self):
        return (self.re*self.re + self.im*self.im) ** 0.5

    def __str__(self) -> str:
        return f'{self.re} + {self.im}i'


complex_numbers = (ComplexNum(1,2), ComplexNum(5,1), ComplexNum(10,0))
mul, sum = ComplexNum(0,0), ComplexNum(0,0)


for num in complex_numbers:
    print(f'Complex num: {num}')
    sum += num
    mul *= num
    print(f'\tTurn 90: {num.turn_90()}')
    print(f'\tModulus: {num.modulus}')

print(f'\nSum: {sum}, Mul: {mul}')
    
