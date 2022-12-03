def first_largest(itarable, number):
    try:
        return next(filter(lambda n: n[1] > number, enumerate(itarable)))[0]
    except StopIteration:
        return -1


if __name__ == '__main__':
    numbers = [10, 2, 14, 7, 7, 18, 20]
    print(first_largest(numbers, 11))

    iterator = iter([18, 21, 14, 72, 73, 18, 20])
    print(first_largest(iterator, 10))

    iterator = iter([-1, -2, -3, -4, -5])
    print(first_largest(iterator, 10))
