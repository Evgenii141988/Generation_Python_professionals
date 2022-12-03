from itertools import dropwhile


def drop_this(iterable, obj):
    return dropwhile(lambda x: x == obj, iterable)


if __name__ == '__main__':
    numbers = [0, 0, 0, 1, 2, 3]
    print(*drop_this(numbers, 0))

    iterator = iter('bbbbeebee')
    print(*drop_this(iterator, 'b'))

    iterator = iter('ssssssssssssssssssssssss')
    print(list(drop_this(iterator, 's')))
