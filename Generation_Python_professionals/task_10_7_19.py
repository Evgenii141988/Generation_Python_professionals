def with_previous(iterable):
    a = None
    for b in iterable:
        a, b = b, a
        yield a, b


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(*with_previous(numbers))

    iterator = iter('stepik')
    print(*with_previous(iterator))

    iterator = iter([])
    print(*with_previous(iterator))
