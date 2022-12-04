from typing import Iterable
from itertools import chain, tee


def ncycles(iterable: Iterable, times: int) -> Iterable:
    return chain(*tee(iterable, times))


if __name__ == '__main__':
    print(*ncycles([1, 2, 3, 4], 3))

    iterator = iter('bee')
    print(*ncycles(iterator, 4))

    iterator = iter([1])

    print(*ncycles(iterator, 10))
