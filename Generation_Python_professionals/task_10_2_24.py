def starmap(func, iterable):
    return map(lambda x: func(*x), iterable)


if __name__ == '__main__':
    pairs = [(1, 3), (2, 5), (6, 4)]

    print(*starmap(lambda a, b: a + b, pairs))

    points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]

    print(*starmap(lambda x, y, z: x * y * z, points))