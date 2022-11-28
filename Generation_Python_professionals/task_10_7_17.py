def unique(iterable):
    return iter({i: i for i in iterable})


if __name__ == '__main__':
    numbers = [1, 2, 2, 3, 4, 5, 5, 5]

    print(*unique(numbers))

    iterator = iter('111222333')
    uniques = unique(iterator)

    print(next(uniques))
    print(next(uniques))
    print(next(uniques))