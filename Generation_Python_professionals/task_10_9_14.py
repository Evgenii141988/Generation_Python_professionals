from itertools import islice


def take(iterable, n):
    return islice(iterable, n)


if __name__ == '__main__':
    print(*take(range(10), 5))

    iterator = iter('beegeek')
    print(*take(iterator, 22))

    iterator = iter('beegeek')
    print(*take(iterator, 1))