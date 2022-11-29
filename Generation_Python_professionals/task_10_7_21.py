def around(iterable):
    try:
        iterator = iter(iterable)
        a = None
        b = next(iterator)
        for c in iterator:
            yield a, b, c
            a, b = b, a
            b, c = c, b
        yield a, b, None
    except StopIteration:
        return


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(*around(numbers))

    iterator = iter('hey')

    print(*around(iterator))

    print(list(around([])))