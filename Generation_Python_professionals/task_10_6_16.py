def count_iterable(iterable):
    try:
        return max(i for i, num in enumerate(iterable, 1))
    except Exception:
        return 0


if __name__ == '__main__':
    print(count_iterable([1, 2, 3, 4, 5]))

    numbers = iter([1, 2, 3, 4, 5, 6, 7])
    print(count_iterable(numbers))

    data = tuple(range(432, 3845, 17))
    print(count_iterable(data))

    data = zip('', '')
    print(count_iterable(data))

    data = filter(None, range(100_000_001))
    print(count_iterable(data))
