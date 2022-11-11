from functools import wraps


def add_attrs(**out_kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        for key, value in out_kwargs.items():
            wrapper.__dict__[key] = value
        return wrapper

    return decorator


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek1():
    return 'beegeek'


if __name__ == '__main__':
    print(beegeek.attr1)
    print(beegeek.attr2)

    print(beegeek1.attr1)
    print(beegeek1.attr2)
    print(beegeek1.__name__)
