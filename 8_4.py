from functools import wraps


def val_checker(validate_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not validate_func(arg):
                    raise(ValueError('Invalid value', arg))
            for key, value in kwargs.items():
                if not validate_func(value):
                    raise(ValueError(f'Invalid value', value))
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

@val_checker(lambda x: x != 0)
def calc_mult(a, b=0):
    return a * b


a = calc_cube(5)

b = calc_mult(5, b = 1)

print(calc_cube.__name__)

print(calc_mult.__name__)
