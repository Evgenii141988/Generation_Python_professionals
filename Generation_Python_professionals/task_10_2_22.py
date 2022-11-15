def get_min_max(data: list) -> tuple:
    if not data:
        return None
    return min(enumerate(data), key=lambda x: x[1])[0], max(enumerate(data), key=lambda x: x[1])[0]


if __name__ == '__main__':
    data = [2, 3, 8, 1, 7]

    print(get_min_max(data))

    data = [9]

    print(get_min_max(data))

    data = [1, 1, 2, 3, 8, 8]

    print(get_min_max(data))