from collections import Counter


def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list[list[int]]:
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(i + 1)
            elif j > i:
                row.append(up_fill)
            else:
                row.append(down_fill)
        result.append(row)
    return result


if __name__ == '__main__':
    print(create_matrix())
    print(create_matrix(4))

