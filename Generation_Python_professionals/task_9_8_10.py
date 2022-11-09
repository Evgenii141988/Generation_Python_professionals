from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result_func = f"'{func(*args, **kwargs)}'" if type(func(*args, **kwargs)) == str else func(*args, **kwargs)
        print(f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}")
        print(f"TRACE: возвращаемое значение {func.__name__}(): {result_func}")
        return func(*args, **kwargs)

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c


@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


if __name__ == '__main__':
    say('Jane', 'Hello, World')

    print(sub.__name__)
    print(sub.__doc__)
    sub(20, 5, c=10)


    @trace
    def beegeek():
        '''beegeek docs'''
        return 'beegeek'


    print(beegeek())
    print(beegeek.__name__)
    print(beegeek.__doc__)
