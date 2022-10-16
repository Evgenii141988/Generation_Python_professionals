def get_pow(a: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return a * get_pow(a, n - 1)


if __name__ == '__main__':
    print(get_pow(5, 2))
    print(get_pow(99, 0))
    print(get_pow(2, 10))