from datetime import date, timedelta


def dates(start: date, count: int = None):
    if count is not None:
        for _ in range(count):
            yield start
            start += timedelta(hours=24)
    else:
        while True:
            try:
                yield start
                start += timedelta(hours=24)
            except OverflowError:
                return


if __name__ == '__main__':
    generator = dates(date(2022, 3, 8))

    print(next(generator))
    print(next(generator))
    print(next(generator))

    generator = dates(date(2022, 3, 8), 5)

    print(*generator)

    generator = dates(date(2024, 9, 13), 1)

    try:
        d = next(generator)
        print(type(d))
        print(d)
        next(generator)
    except StopIteration:
        print('Error')

    generator = dates(date(9999, 1, 7))

    for _ in range(348):
        next(generator)

    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))

    try:
        print(next(generator))
    except StopIteration:
        print('Error')