from functools import wraps


def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) != str:
            raise TypeError
        return result

    return wrapper


@returns_string
def beegeek():
    return 'beegeek'


@returns_string
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(beegeek())

    try:
        print(add(3, 7))
    except TypeError as e:
        print(type(e))
