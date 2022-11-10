from functools import wraps


def prefix(string: str, to_the_end: bool = False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return func(*args, **kwargs) + string
            return string + func(*args, **kwargs)

        return wrapper

    return decorator


@prefix('€')
def get_bonus():
    return '2000'


@prefix('$$$', to_the_end=True)
def get_bonus1():
    return '2000'


if __name__ == '__main__':
    print(get_bonus())
    print(get_bonus1())
