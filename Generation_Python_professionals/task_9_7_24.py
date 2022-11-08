def takes_positive(func):
    def wrapper(*args, **kwargs):
        if any((type(num) != int for num in args)) or any((type(value) != int for value in kwargs.values())):
            raise TypeError
        if any((type(num) == int and num <= 0 for num in args)) or any(
                (type(value) == int and value <= 0 for value in kwargs.values())):
            raise ValueError
        return func(*args, **kwargs)

    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


@takes_positive
def positive_sum1(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


if __name__ == '__main__':
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    try:
        print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
    except Exception as err:
        print(type(err))

    try:
        print(positive_sum('10', 20, 10))
    except Exception as err:
        print(type(err))

    try:
        print(positive_sum1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
    except Exception as err:
        print(type(err))
