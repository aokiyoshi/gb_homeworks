from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f'{func.__name__} ({arg}: {type(arg)})')
        for key, value in kwargs.items():
            print(f'{func.__name__} {key}: {value}: {type(value)})')

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_mult(a, b=0):
    return a * b


a = calc_cube(5)
b = calc_mult(a = 5, b = 100)
print(calc_cube.__name__)