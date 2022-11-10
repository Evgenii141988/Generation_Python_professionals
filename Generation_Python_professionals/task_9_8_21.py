from functools import wraps


def returns(datatype: type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if not type(value) == datatype:
                raise TypeError
            return value

        return wrapper

    return decorator


@returns(int)
def add(a, b):
    return a + b


@returns(list)
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


@returns(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]


if __name__ == '__main__':
    print(add(10, 5))

    try:
        print(add('199', '1'))
    except TypeError as e:
        print(type(e))

    print(beegeek.__name__)
    print(beegeek.__doc__)

    try:
        print(beegeek())
    except TypeError as e:
        print(type(e))

    print(append_this.__name__)
    print(append_this.__doc__)
    print(append_this([1, 2, 3], elem=4))