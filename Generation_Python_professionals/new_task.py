from functools import wraps


# Напишите определение декоратора validate_args
def validate_args(func):
    @wraps(func)
    def inner(*args, **kwargs):
        match args:
            case (int(), int()):
                return func(*args, **kwargs)
            case a, :
                return 'No enough arguments'
            case a, b, c, *_:
                return 'Too many arguments'
            case _:
                return 'Wrong types'

    return inner


# Код ниже не удаляйте, он нужен для проверки   
@validate_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


if __name__ == '__main__':
    assert add_numbers(4, 5) == 9
    assert add_numbers(4) == 'No enough arguments'
    assert add_numbers('hello') == 'No enough arguments'
    assert add_numbers(3, 5, 6) == 'Too many arguments'
    assert add_numbers('a', 'b', 'c') == 'Too many arguments'
    assert add_numbers(4.5, 5.1) == 'Wrong types'
    assert add_numbers('hello', 4) == 'Wrong types'
    assert add_numbers(9, 'hello') == 'Wrong types'
    assert add_numbers([1, 3], {}) == 'Wrong types'
    assert add_numbers.__name__ == 'add_numbers'
    assert add_numbers.__doc__.strip() == 'Return sum of x and y'
    print('Good')
