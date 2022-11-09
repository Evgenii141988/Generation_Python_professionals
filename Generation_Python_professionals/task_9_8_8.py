from functools import wraps


def square(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result ** 2

    return wrapper


@square
def add(a, b):
    '''прекрасная функция'''
    return a + b


if __name__ == '__main__':
    print(add(3, 7))
    print(add(1, 1))
    print(add.__name__)
    print(add.__doc__)