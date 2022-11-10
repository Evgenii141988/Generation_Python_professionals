from functools import wraps


def strip_range(start: int, end: int, char: str = '.'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            for i in range(start, end if len(value) >= end else len(value)):
                value = value[:i] + char + value[i + 1:]
            return value

        return wrapper

    return decorator


@strip_range(3, 5)
def beegeek():
    return 'beegeek'


@strip_range(3, 20, '_')
def beegeek1():
    return 'beegeek'


@strip_range(20, 30)
def beegeek2():
    return 'beegeek'


if __name__ == '__main__':
    print(beegeek())
    print(beegeek1())
    print(beegeek2())
