from itertools import pairwise


def is_rising(iterable):
    return all(b > a for a, b in pairwise(iterable))


if __name__ == '__main__':
    print(is_rising([1, 2, 3, 4, 5]))

    iterator = iter([1, 1, 1, 2, 3, 4])

    print(is_rising(iterator))

    iterator = iter(list(range(100, 200)))

    print(is_rising(iterator))