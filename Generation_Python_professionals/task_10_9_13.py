def first_true(iterable, predicate):
    try:
        return next(filter(predicate, iterable))
    except StopIteration:
        return None


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 2, 4, 5, 6]
    print(first_true(numbers, lambda num: num % 2 == 0))

    numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
    print(first_true(numbers, lambda num: num > 10))

    numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
    print(first_true(numbers, None))