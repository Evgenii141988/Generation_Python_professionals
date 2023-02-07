
def only_one_positive(*args: [int | float]) -> str:
    return len([n for n in args if n > 0]) == 1


if __name__ == '__main__':
    print(only_one_positive(-1, 0, -3, 5, -3))
    print(only_one_positive(1, 2))
    print(only_one_positive())
