from functools import reduce


def multiply(*args: [int | float]) -> str:
    return reduce(lambda x, y: x * y, args, 1)


if __name__ == '__main__':
    print(multiply(8, 11))
    print(multiply(10, 10, 10, 10, 9))
