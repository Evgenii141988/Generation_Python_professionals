from functools import wraps


def repeat(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times - 1):
                func(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')


if __name__ == '__main__':
    say_beegeek()

    print(say_beegeek.__name__)
    print(say_beegeek.__doc__)