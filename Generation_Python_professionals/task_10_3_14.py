def is_iterable(obj: object) -> bool:
    return '__iter__' in dir(obj)


if __name__ == '__main__':
    print(is_iterable(18731))
    print(is_iterable('18731'))

    objects = [(1, 13), 7.0004, [1, 2, 3]]

    for obj in objects:
        print(is_iterable(obj))