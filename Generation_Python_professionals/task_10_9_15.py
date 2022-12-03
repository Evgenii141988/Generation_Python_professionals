from itertools import islice


def take_nth(iterable, n):
    try:
        return next(islice(iterable, n - 1, n))
    except StopIteration:
        return None


if __name__ == '__main__':
    numbers = [11, 22, 33, 44, 55]
    print(take_nth(numbers, 3))

    iterator = iter('beegeek')
    print(take_nth(iterator, 4))

    iterator = iter('beegeek')
    print(take_nth(iterator, 10))
