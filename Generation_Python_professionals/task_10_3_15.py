def is_iterator(obj: object) -> bool:
    return hasattr(obj, '__next__')


if __name__ == '__main__':
    print(is_iterator([1, 2, 3, 4, 5]))

    beegeek = map(str.upper, 'beegeek')

    print(is_iterator(beegeek))

    beegeek = filter(None, [0, 0, 1, 1, 0, 1])

    print(is_iterator(beegeek))