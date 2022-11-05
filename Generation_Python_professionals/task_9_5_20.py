def sort_priority(values: list, group: (list, tuple, set)):
    def inner(num: int):
        if num in group:
            return 0, num
        return 1, num

    return values.sort(key=inner)


if __name__ == '__main__':
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {5, 7, 2, 3}
    sort_priority(numbers, group)

    print(numbers)

    numbers = [150, 200, 300, 1000, 50, 20000]
    sort_priority(numbers, [300, 100, 200])

    print(numbers)

    numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort_priority(numbers, (300, 100, 200))

    print(numbers)