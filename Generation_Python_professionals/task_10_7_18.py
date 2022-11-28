def stop_on(iterable, obj):
    for elm in iterable:
        if elm == obj:
            return
        yield elm


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(*stop_on(numbers, 4))

    iterator = iter('beegeek')

    print(*stop_on(iterator, 'a'))
