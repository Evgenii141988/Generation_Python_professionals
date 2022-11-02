def print_operation_table(operation, rows: int, cols: int):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(operation(i, j), end=' ')
        print()


if __name__ == '__main__':
    print_operation_table(lambda a, b: a * b, 5, 5)
    print()
    print_operation_table(pow, 5, 4)