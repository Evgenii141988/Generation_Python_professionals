def is_greater(lists: list[list], number: int) -> bool:
    return any([sum(lst) > number for lst in lists])


if __name__ == '__main__':
    data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]

    print(is_greater(data, 10))
    data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

    print(is_greater(data, 2))
    data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]

    print(is_greater(data, 3))