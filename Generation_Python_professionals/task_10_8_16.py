from itertools import accumulate
import operator


def factorials(n):
    return accumulate(range(1, n + 1), operator.mul)


if __name__ == '__main__':
    numbers = factorials(6)
    print(*numbers)

    numbers = factorials(2)

    print(next(numbers))
    print(next(numbers))