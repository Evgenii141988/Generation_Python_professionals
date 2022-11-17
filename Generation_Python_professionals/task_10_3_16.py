from random import randint


def random_numbers(left: int, right: int) -> iter:
    return iter(lambda: randint(left, right), 'python')


if __name__ == '__main__':
    iterator = random_numbers(1, 1)

    print(next(iterator))
    print(next(iterator))

    iterator = random_numbers(1, 10)

    print(next(iterator) in range(1, 11))
    print(next(iterator) in range(1, 11))
    print(next(iterator) in range(1, 11))
