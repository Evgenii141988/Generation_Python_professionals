from typing import Iterable
from itertools import repeat, zip_longest


def grouper(iterable: Iterable, n: int) -> Iterable:
    iterator = iter(iterable)
    return zip_longest(*repeat(iterator, n))


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6]
    print(*grouper(numbers, 2))

    iterator = iter([1, 2, 3, 4, 5, 6, 7])

    print(*grouper(iterator, 3))

    iterator = iter([1, 2, 3])

    print(*grouper(iterator, 5))

