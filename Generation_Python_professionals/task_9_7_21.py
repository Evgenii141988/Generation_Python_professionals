def do_twice(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        func(*args, **kwargs)
        return result
    return wrapper


@do_twice
def beegeek():
    print('beegeek')


@do_twice
def beegeek1():
    return 'beegeek'


if __name__ == '__main__':
    beegeek()
    print()
    print(beegeek())
    print()
    print(beegeek1())


