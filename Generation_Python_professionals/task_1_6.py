def print_from(n: int) -> None:
    if n > 0:
        print(n)
        print_from(n - 1)


if __name__ == '__main__':
    print_from(4)
    print_from(7)
