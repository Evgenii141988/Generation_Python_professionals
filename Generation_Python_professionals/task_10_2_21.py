def transpose(matrix: list[list]):
    return list(list(elm) for elm in zip(*matrix))


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    for row in transpose(matrix):
        print(row)

    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10]]

    for row in transpose(matrix):
        print(row)
